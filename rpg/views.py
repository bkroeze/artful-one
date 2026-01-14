"""Views for RPG app."""

import json

from django.core import signing
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rpg.models import RpgTable
from rpg.roller import generate


# Constants
COOKIE_NAME = "rpg_favorites"
MAX_FAVORITES = 50
COOKIE_MAX_AGE_DAYS = 365


def get_favorites(request: HttpRequest) -> list[dict]:
    """Get favorites from signed cookie.

    Returns a list of dicts with keys: name, table, addon
    """
    favorites = []
    cookie_value = request.COOKIES.get(COOKIE_NAME, "")

    if cookie_value:
        try:
            # Signer requires a key - use Django's SECRET_KEY
            signer = signing.Signer()
            decoded = signer.unsign(cookie_value)
            favorites = json.loads(decoded)
            if not isinstance(favorites, list):
                favorites = []
        except (signing.BadSignature, json.JSONDecodeError):
            favorites = []

    return favorites


def set_favorites_cookie(response: HttpResponse, favorites: list[dict]) -> HttpResponse:
    """Set the signed cookie with favorites data.

    Args:
        response: HttpResponse to modify
        favorites: List of favorite dicts

    Returns:
        Modified HttpResponse
    """
    # Limit to max favorites
    favorites = favorites[:MAX_FAVORITES]

    # Encode as JSON and sign
    value = json.dumps(favorites)
    signer = signing.Signer()
    signed_value = signer.sign(value)

    # Set cookie
    response.set_cookie(
        COOKIE_NAME,
        signed_value,
        max_age=COOKIE_MAX_AGE_DAYS * 24 * 60 * 60,
        httponly=True,
        samesite="Lax",
    )

    return response


def root(request: HttpRequest) -> HttpResponse:
    """Root page for the RPG app.

    Redirects to names page.
    """
    from django.http import HttpResponseRedirect

    return HttpResponseRedirect("/rpg/names/")


def rpg_names_page(request: HttpRequest) -> HttpResponse:
    """Main RPG names page with HTMX-powered generation.

    Supports two table sets:
    - names: Table names from names.ts
    - adventure-design: Adventure design tables from adventure-design.ts
    """
    # Get table set from query param or default to 'names'
    table_set = request.GET.get("set", "names")

    # Get available tables (non-hidden, filtered by set)
    tables_query = RpgTable.objects.filter(hidden=False)

    if table_set == "adventure-design":
        tables_query = tables_query.filter(slug__startswith="ad/")
    elif table_set == "names":
        tables_query = tables_query.filter(slug__startswith="names/")
    # else: don't filter, show all

    tables = tables_query.order_by("slug")

    # Get favorites
    favorites = get_favorites(request)

    context = {
        "tables": tables,
        "table_set": table_set,
        "favorites": favorites,
    }

    response = render(request, "rpg/rpg-names.html", context)
    return response


@csrf_exempt
def htmx_generate(request: HttpRequest) -> HttpResponse:
    """HTMX endpoint to generate names.

    POST parameters:
    - table: Table alias or template
    - count: Number of names to generate (default: 10)
    - addon: Optional addon key (e.g., "epithets", "forest")

    Returns:
        HTML fragment with generated names
    """
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    table_alias = request.POST.get("table", "")
    count = int(request.POST.get("count", 10))
    addon = request.POST.get("addon", "") or None

    if not table_alias:
        return HttpResponse('<div class="ui error message">No table specified</div>')

    try:
        names = generate(table_alias, count=count, addon_key=addon)
    except Exception as e:
        return HttpResponse(
            f'<div class="ui error message">Error generating names: {e}</div>'
        )

    context = {"names": names, "table_alias": table_alias, "addon": addon}

    return render(request, "rpg/partials/names_table.html", context)


def htmx_favorites(request: HttpRequest) -> HttpResponse:
    """HTMX endpoint to render favorites list.

    Returns:
        HTML fragment with favorites list
    """
    favorites = get_favorites(request)
    context = {"favorites": favorites}
    return render(request, "rpg/partials/favorites_list.html", context)


@csrf_exempt
def htmx_toggle_favorite(request: HttpRequest) -> HttpResponse:
    """HTMX endpoint to toggle a favorite.

    POST parameters:
    - name: Generated name to save/remove
    - table: Table alias used
    - addon: Optional addon key used

    Returns:
        HTML fragment with updated favorites list
    """
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)

    name = request.POST.get("name", "")
    table_alias = request.POST.get("table", "")
    addon = request.POST.get("addon", "")

    if not name or not table_alias:
        return HttpResponse("Missing required parameters", status=400)

    favorites = get_favorites(request)

    # Check if this already exists in favorites
    exists = False
    for i, fav in enumerate(favorites):
        if fav.get("name") == name and fav.get("table") == table_alias:
            exists = True
            favorites.pop(i)  # Remove it
            break

    if not exists:
        # Add new favorite
        favorites.append({"name": name, "table": table_alias, "addon": addon})

    response = render(
        request,
        "rpg/partials/favorites_list.html",
        {"favorites": favorites},
    )

    return set_favorites_cookie(response, favorites)
