import json
from urllib.parse import urlsplit
from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import FileSystemStorage
from django.test import Client
from django.utils import timezone

from sketches.models import SketchToken, TemporarySketchMedia, WorkingSketch


def issue_token(user):
    token, raw_token = SketchToken.issue(user, "test agent")
    return token, raw_token, {"HTTP_AUTHORIZATION": f"Bearer {raw_token}"}


@pytest.mark.django_db
def test_bearer_crud_is_owner_scoped_and_rejects_duplicate_slugs(client):
    user_model = get_user_model()
    owner = user_model.objects.create_user("owner")
    other = user_model.objects.create_user("other")
    admin = user_model.objects.create_user("admin", is_staff=True)
    token, raw_token, owner_auth = issue_token(owner)
    _other_token, _other_raw, other_auth = issue_token(other)
    _admin_token, _admin_raw, admin_auth = issue_token(admin)

    assert raw_token not in token.digest
    assert token.matches(raw_token)

    payload = {
        "slug": "orbit",
        "title": "Orbit",
        "sketch_type": "d3",
        "startup_js": "root.dataset.started = 'yes';",
        "div_html": '<div id="provided"><svg></svg></div>',
    }
    response = client.post(
        "/sketchy/api/sketches/",
        data=json.dumps(payload),
        content_type="application/json",
        **owner_auth,
    )
    assert response.status_code == 201
    assert response.json()["sketch"]["startup_js"] == payload["startup_js"]
    assert response.json()["sketch"]["owner"]["username"] == owner.username

    duplicate = client.post(
        "/sketchy/api/sketches/",
        data=json.dumps(payload),
        content_type="application/json",
        **other_auth,
    )
    assert duplicate.status_code == 409
    assert duplicate.json()["error"]["code"] == "slug_conflict"

    assert client.get("/sketchy/api/sketches/", **other_auth).json()["count"] == 0
    assert client.get("/sketchy/api/sketches/", **admin_auth).json()["count"] == 1
    assert client.get("/sketchy/api/sketches/orbit/", **other_auth).status_code == 404

    updated = client.patch(
        "/sketchy/api/sketches/orbit/",
        data=json.dumps({"title": "Updated Orbit"}),
        content_type="application/json",
        **owner_auth,
    )
    assert updated.status_code == 200
    assert updated.json()["sketch"]["title"] == "Updated Orbit"
    assert (
        client.delete("/sketchy/api/sketches/orbit/", **owner_auth).status_code == 200
    )
    assert not WorkingSketch.objects.filter(slug="orbit").exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("sketch_type", "runtime_marker"),
    [
        ("d3", "d3@7.9.0"),
        ("processing", "new Processing(canvas"),
        ("raw", 'new Function("root", source)'),
    ],
)
def test_private_page_normalizes_root_and_loads_runtime(
    client, sketch_type, runtime_marker
):
    user_model = get_user_model()
    owner = user_model.objects.create_user(f"owner-{sketch_type}")
    other = user_model.objects.create_user(f"other-{sketch_type}")
    _token, _raw_token, bearer = issue_token(owner)
    WorkingSketch.objects.create(
        owner=owner,
        slug=f"runtime-{sketch_type}",
        title="Runtime",
        sketch_type=sketch_type,
        startup_js="root.dataset.started = 'yes';",
        div_html='<div id="provided"><span id="sketch-root"></span></div>',
    )
    url = f"/sketchy/sketches/runtime-{sketch_type}"

    assert client.get(url).status_code == 404
    client.force_login(other)
    assert client.get(url).status_code == 404
    assert client.get(url, **bearer).status_code == 200
    client.logout()

    response = client.get(url, **bearer)
    assert response.status_code == 200
    content = response.content.decode()
    assert runtime_marker in content
    assert content.count('id="sketch-root"') == 1
    assert 'id="provided"' not in content
    assert "sandbox allow-scripts" in response.headers["Content-Security-Policy"]
    assert "allow-same-origin" not in response.headers["Content-Security-Policy"]
    assert response.headers["X-Robots-Tag"] == "noindex, nofollow, noarchive"

    owner.is_active = False
    owner.save(update_fields=("is_active",))
    assert Client().get(url, **bearer).status_code == 404


@pytest.mark.django_db(transaction=True)
def test_temporary_media_is_scoped_signed_and_deleted(client, monkeypatch, tmp_path):
    storage = FileSystemStorage(location=tmp_path)
    file_field = TemporarySketchMedia._meta.get_field("file")
    monkeypatch.setattr(file_field, "storage", storage)
    user_model = get_user_model()
    owner = user_model.objects.create_user("media-owner")
    other = user_model.objects.create_user("media-other")
    _token, _raw_token, owner_auth = issue_token(owner)
    _other_token, _other_raw, other_auth = issue_token(other)
    sketch = WorkingSketch.objects.create(
        owner=owner,
        slug="rigged",
        title="Rigged",
        sketch_type="raw",
    )

    upload = SimpleUploadedFile("rig.html", b"frame-data", content_type="text/html")
    response = client.post(
        "/sketchy/api/media/",
        {"file": upload, "sketch": sketch.slug, "expires_in_hours": "2"},
        **owner_auth,
    )
    assert response.status_code == 201
    media_data = response.json()["media"]
    assert media_data["reference"].startswith("sketchy-media://")
    assert (
        client.get(f"/sketchy/api/media/{media_data['id']}/", **other_auth).status_code
        == 404
    )

    media = TemporarySketchMedia.objects.get(pk=media_data["id"])
    stored_name = media.file.name
    assert media.file.storage.exists(stored_name)
    assert client.get(f"/media/{stored_name}").status_code == 404

    sketch.div_html = f'<div><img src="{media_data["reference"]}"></div>'
    sketch.save()
    page = client.get(sketch.get_absolute_url(), **owner_auth)
    content = page.content.decode()
    assert "sketchy-media://" not in content
    signed_url = content.split('src="', 1)[1].split('"', 1)[0]
    signed_asset = Client().get(signed_url)
    assert signed_asset.status_code == 200
    assert b"".join(signed_asset.streaming_content) == b"frame-data"
    assert (
        signed_asset.headers["Content-Security-Policy"] == "sandbox; default-src 'none'"
    )
    assert signed_asset.headers["Access-Control-Allow-Origin"] == "null"
    assert Client().get(urlsplit(media_data["url"]).path).status_code == 404

    expired = TemporarySketchMedia.objects.create(
        owner=owner,
        file=SimpleUploadedFile("expired.txt", b"old"),
        original_name="expired.txt",
        content_type="text/plain",
        size=3,
        expires_at=timezone.now() - timedelta(seconds=1),
    )
    expired_name = expired.file.name
    listing = client.get("/sketchy/api/media/", **owner_auth)
    assert listing.status_code == 200
    assert listing.json()["count"] == 1
    assert not TemporarySketchMedia.objects.filter(pk=expired.pk).exists()
    assert not storage.exists(expired_name)

    deleted = client.delete(f"/sketchy/api/media/{media.pk}/", **owner_auth)
    assert deleted.status_code == 200
    assert not TemporarySketchMedia.objects.filter(pk=media.pk).exists()
    assert not media.file.storage.exists(stored_name)
