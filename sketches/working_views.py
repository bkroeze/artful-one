import secrets
import json
import re
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlencode

from bs4 import BeautifulSoup, Tag
from django.core import signing
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.db import IntegrityError, transaction
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import SketchToken, TemporarySketchMedia, WorkingSketch

MEDIA_REFERENCE_RE = re.compile(
    r"sketchy-media://([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"
)
MEDIA_URL_MAX_AGE = 60 * 60
MAX_MEDIA_BYTES = 25 * 1024 * 1024


def _error(code, message, status):
    return JsonResponse({"error": {"code": code, "message": message}}, status=status)


def _bearer_user(request):
    authorization = request.headers.get("Authorization", "")
    scheme, separator, raw_token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not separator or not raw_token:
        return None

    token = (
        SketchToken.objects.select_related("user")
        .filter(prefix=raw_token[:16], active=True)
        .first()
    )
    if token is None or not token.matches(raw_token):
        return None
    if token.expires_at is not None and token.expires_at <= timezone.now():
        return None

    now = timezone.now()
    if token.last_used_at is None or token.last_used_at < now - timedelta(minutes=5):
        SketchToken.objects.filter(pk=token.pk).update(last_used_at=now)
    return token.user


def _api_user(request):
    user = _bearer_user(request)
    if user is None or not user.is_active:
        return None
    return user


def _page_user(request):
    bearer_user = _bearer_user(request)
    if bearer_user is not None and bearer_user.is_active:
        return bearer_user
    if request.user.is_authenticated and request.user.is_active:
        return request.user
    return None


def _visible_sketches(user):
    queryset = WorkingSketch.objects.select_related("owner")
    if user.is_staff:
        return queryset
    return queryset.filter(owner=user)


def _visible_media(user):
    queryset = TemporarySketchMedia.objects.select_related("owner", "sketch").filter(
        expires_at__gt=timezone.now()
    )
    if user.is_staff:
        return queryset
    return queryset.filter(owner=user)


def _purge_expired_media():
    TemporarySketchMedia.objects.filter(expires_at__lte=timezone.now()).delete()


def _iso(value):
    return value.isoformat() if value is not None else None


def _serialize_sketch(request, sketch):
    return {
        "id": sketch.pk,
        "owner": {"id": sketch.owner_id, "username": sketch.owner.get_username()},
        "slug": sketch.slug,
        "title": sketch.title,
        "sketch_type": sketch.sketch_type,
        "startup_js": sketch.startup_js,
        "div_html": sketch.div_html,
        "created_at": _iso(sketch.created_at),
        "updated_at": _iso(sketch.updated_at),
        "url": request.build_absolute_uri(sketch.get_absolute_url()),
    }


def _media_reference(media):
    return f"sketchy-media://{media.pk}"


def _serialize_media(request, media):
    return {
        "id": str(media.pk),
        "owner": {"id": media.owner_id, "username": media.owner.get_username()},
        "sketch": media.sketch.slug if media.sketch_id else None,
        "original_name": media.original_name,
        "content_type": media.content_type,
        "size": media.size,
        "created_at": _iso(media.created_at),
        "expires_at": _iso(media.expires_at),
        "reference": _media_reference(media),
        "url": request.build_absolute_uri(
            reverse(
                "working_sketch_media",
                kwargs={"media_id": media.pk, "filename": media.original_name},
            )
        ),
    }


def _json_body(request):
    try:
        payload = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None, _error("invalid_json", "Request body must be valid JSON.", 400)
    if not isinstance(payload, dict):
        return None, _error("invalid_json", "Request body must be a JSON object.", 400)
    return payload, None


def _validate_sketch_payload(payload, *, creating):
    allowed = {"slug", "title", "sketch_type", "startup_js", "div_html"}
    unknown = sorted(set(payload) - allowed)
    if unknown:
        return f"Unknown field(s): {', '.join(unknown)}."

    required = {"slug", "title", "sketch_type"}
    missing = sorted(field for field in required if creating and field not in payload)
    if missing:
        return f"Missing required field(s): {', '.join(missing)}."

    if "slug" in payload:
        if not isinstance(payload["slug"], str) or not payload["slug"]:
            return "slug must be a non-empty string."
        if len(payload["slug"]) > 255:
            return "slug must be at most 255 characters."
        try:
            validate_slug(payload["slug"])
        except ValidationError:
            return "slug may contain only letters, numbers, underscores, and hyphens."

    if "title" in payload and (
        not isinstance(payload["title"], str) or not payload["title"].strip()
    ):
        return "title must be a non-empty string."
    if "title" in payload and len(payload["title"]) > 255:
        return "title must be at most 255 characters."

    if "sketch_type" in payload and payload["sketch_type"] not in {
        choice for choice, _label in WorkingSketch.SketchType.choices
    }:
        return "sketch_type must be one of: d3, processing, raw."

    for field in ("startup_js", "div_html"):
        if field in payload and not isinstance(payload[field], str):
            return f"{field} must be a string."
    return None


@csrf_exempt
def working_sketch_collection(request):
    user = _api_user(request)
    if user is None:
        return _error(
            "authentication_required",
            "Provide a valid bearer token in the Authorization header.",
            401,
        )

    if request.method == "GET":
        sketches = list(_visible_sketches(user).order_by("-updated_at"))
        return JsonResponse(
            {
                "count": len(sketches),
                "sketches": [_serialize_sketch(request, sketch) for sketch in sketches],
            }
        )

    if request.method != "POST":
        return _error("method_not_allowed", "Use GET or POST on this endpoint.", 405)

    payload, error_response = _json_body(request)
    if error_response is not None:
        return error_response
    validation_error = _validate_sketch_payload(payload, creating=True)
    if validation_error:
        return _error("invalid_sketch", validation_error, 400)

    try:
        with transaction.atomic():
            sketch = WorkingSketch.objects.create(
                owner=user,
                slug=payload["slug"],
                title=payload["title"].strip(),
                sketch_type=payload["sketch_type"],
                startup_js=payload.get("startup_js", ""),
                div_html=payload.get("div_html", ""),
            )
    except IntegrityError:
        return _error(
            "slug_conflict",
            f'A sketch with slug "{payload["slug"]}" already exists.',
            409,
        )
    return JsonResponse({"sketch": _serialize_sketch(request, sketch)}, status=201)


@csrf_exempt
def working_sketch_item(request, slug):
    user = _api_user(request)
    if user is None:
        return _error(
            "authentication_required",
            "Provide a valid bearer token in the Authorization header.",
            401,
        )

    try:
        sketch = _visible_sketches(user).get(slug=slug)
    except WorkingSketch.DoesNotExist:
        return _error("not_found", f'No visible sketch has slug "{slug}".', 404)

    if request.method == "GET":
        return JsonResponse({"sketch": _serialize_sketch(request, sketch)})

    if request.method == "DELETE":
        deleted_slug = sketch.slug
        sketch.delete()
        return JsonResponse({"deleted": {"slug": deleted_slug}})

    if request.method not in {"PATCH", "PUT"}:
        return _error("method_not_allowed", "Use GET, PATCH, PUT, or DELETE.", 405)

    payload, error_response = _json_body(request)
    if error_response is not None:
        return error_response
    validation_error = _validate_sketch_payload(
        payload, creating=request.method == "PUT"
    )
    if validation_error:
        return _error("invalid_sketch", validation_error, 400)

    for field in ("slug", "title", "sketch_type", "startup_js", "div_html"):
        if field in payload:
            value = payload[field]
            if field == "title":
                value = value.strip()
            setattr(sketch, field, value)
    try:
        with transaction.atomic():
            sketch.save()
    except IntegrityError:
        return _error(
            "slug_conflict",
            f'A sketch with slug "{payload.get("slug")}" already exists.',
            409,
        )
    return JsonResponse({"sketch": _serialize_sketch(request, sketch)})


@csrf_exempt
def working_media_collection(request):
    user = _api_user(request)
    if user is None:
        return _error(
            "authentication_required",
            "Provide a valid bearer token in the Authorization header.",
            401,
        )

    _purge_expired_media()

    if request.method == "GET":
        media_items = list(_visible_media(user).order_by("-created_at"))
        return JsonResponse(
            {
                "count": len(media_items),
                "media": [_serialize_media(request, media) for media in media_items],
            }
        )

    if request.method != "POST":
        return _error("method_not_allowed", "Use GET or POST on this endpoint.", 405)

    upload = request.FILES.get("file")
    if upload is None:
        return _error("file_required", "Upload one file using the file field.", 400)
    if upload.size > MAX_MEDIA_BYTES:
        return _error("file_too_large", "Temporary media is limited to 25 MiB.", 400)

    sketch = None
    sketch_slug = request.POST.get("sketch")
    if sketch_slug:
        try:
            sketch = _visible_sketches(user).get(slug=sketch_slug)
        except WorkingSketch.DoesNotExist:
            return _error(
                "sketch_not_found",
                f'No visible sketch has slug "{sketch_slug}".',
                404,
            )
        if sketch.owner_id != user.pk:
            return _error("forbidden", "You cannot attach media to that sketch.", 403)

    expires_in = request.POST.get("expires_in_hours", "168")
    try:
        expires_in_hours = int(expires_in)
    except ValueError:
        return _error("invalid_expiry", "expires_in_hours must be an integer.", 400)
    if not 1 <= expires_in_hours <= 720:
        return _error(
            "invalid_expiry", "expires_in_hours must be between 1 and 720.", 400
        )

    media = TemporarySketchMedia.objects.create(
        owner=user,
        sketch=sketch,
        file=upload,
        original_name=Path(upload.name).name,
        content_type=upload.content_type or "application/octet-stream",
        size=upload.size,
        expires_at=timezone.now() + timedelta(hours=expires_in_hours),
    )
    return JsonResponse({"media": _serialize_media(request, media)}, status=201)


@csrf_exempt
def working_media_item(request, media_id):
    user = _api_user(request)
    if user is None:
        return _error(
            "authentication_required",
            "Provide a valid bearer token in the Authorization header.",
            401,
        )
    try:
        media = _visible_media(user).get(pk=media_id)
    except (TemporarySketchMedia.DoesNotExist, ValidationError, ValueError):
        return _error("not_found", f'No visible media has id "{media_id}".', 404)

    if request.method == "GET":
        return JsonResponse({"media": _serialize_media(request, media)})
    if request.method == "DELETE":
        media_id_string = str(media.pk)
        media.delete()
        return JsonResponse({"deleted": {"id": media_id_string}})
    return _error("method_not_allowed", "Use GET or DELETE on this endpoint.", 405)


def _normalize_sketch_body(fragment):
    soup = BeautifulSoup(fragment or "", "html.parser")
    root_tags = [child for child in soup.contents if isinstance(child, Tag)]
    text_outside_root = any(
        not isinstance(child, Tag) and str(child).strip() for child in soup.contents
    )

    if (
        len(root_tags) == 1
        and not text_outside_root
        and root_tags[0].name
        in {
            "div",
            "canvas",
        }
    ):
        root = root_tags[0]
        root["id"] = "sketch-root"
    else:
        wrapper_soup = BeautifulSoup('<div id="sketch-root"></div>', "html.parser")
        root = wrapper_soup.div
        for child in list(soup.contents):
            root.append(child.extract())
        soup = wrapper_soup

    for duplicate in root.select("#sketch-root"):
        if duplicate is not root:
            del duplicate["id"]
    return str(soup)


def _signed_media_url(media):
    signature = signing.TimestampSigner(salt="sketchy.media").sign(str(media.pk))
    path = reverse(
        "working_sketch_media",
        kwargs={"media_id": media.pk, "filename": media.original_name},
    )
    return f"{path}?{urlencode({'signature': signature})}"


def _resolve_media_references(content, sketch):
    ids = set(MEDIA_REFERENCE_RE.findall(content))
    if not ids:
        return content
    now = timezone.now()
    media_by_id = {
        str(media.pk): media
        for media in TemporarySketchMedia.objects.filter(
            pk__in=ids,
            owner=sketch.owner,
            expires_at__gt=now,
        ).select_related("sketch")
        if media.sketch_id is None or media.sketch_id == sketch.pk
    }
    return MEDIA_REFERENCE_RE.sub(
        lambda match: (
            _signed_media_url(media_by_id[match.group(1)])
            if match.group(1) in media_by_id
            else match.group(0)
        ),
        content,
    )


def working_sketch_detail(request, slug):
    user = _page_user(request)
    if user is None:
        raise Http404
    try:
        sketch = _visible_sketches(user).get(slug=slug)
    except WorkingSketch.DoesNotExist as error:
        raise Http404 from error

    sketch_body = _resolve_media_references(
        _normalize_sketch_body(sketch.div_html), sketch
    )
    startup_js = _resolve_media_references(sketch.startup_js, sketch)
    response = render(
        request,
        "working_sketch_detail.html",
        {"sketch": sketch, "sketch_body": sketch_body, "startup_js": startup_js},
    )
    response["Cache-Control"] = "private, no-store"
    response["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    response["X-Frame-Options"] = "DENY"
    response["Content-Security-Policy"] = (
        "sandbox allow-scripts; default-src 'none'; "
        "script-src 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; "
        "style-src 'unsafe-inline' https: http:; "
        "img-src https: http: data: blob:; media-src https: http: data: blob:; "
        "font-src https: http: data:; connect-src https: http:; form-action 'none'"
    )
    return response


def working_sketch_media(request, media_id, filename):
    try:
        media = TemporarySketchMedia.objects.select_related("owner").get(pk=media_id)
    except (TemporarySketchMedia.DoesNotExist, ValidationError, ValueError) as error:
        raise Http404 from error
    if media.expires_at <= timezone.now():
        media.delete()
        raise Http404

    permitted = False
    signature = request.GET.get("signature")
    if signature:
        try:
            signed_id = signing.TimestampSigner(salt="sketchy.media").unsign(
                signature, max_age=MEDIA_URL_MAX_AGE
            )
            permitted = secrets.compare_digest(signed_id, str(media.pk))
        except signing.BadSignature:
            permitted = False
    if not permitted:
        user = _page_user(request)
        permitted = user is not None and (user.is_staff or user.pk == media.owner_id)
    if not permitted:
        raise Http404

    response = FileResponse(
        media.file.open("rb"),
        content_type=media.content_type or "application/octet-stream",
        as_attachment=False,
        filename=media.original_name,
    )
    response["Cache-Control"] = "private, max-age=3600"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Security-Policy"] = "sandbox; default-src 'none'"
    response["Cross-Origin-Resource-Policy"] = "cross-origin"
    if signature:
        response["Access-Control-Allow-Origin"] = "null"
    return response
