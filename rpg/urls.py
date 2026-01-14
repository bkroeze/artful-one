"""URL configuration for RPG app."""

from django.urls import path

from rpg import views as rpg_views

app_name = "rpg"

urlpatterns = [
    path("", rpg_views.root, name="root"),
    path("names/", rpg_views.rpg_names_page, name="names"),
    path("names/generate/", rpg_views.htmx_generate, name="htmx_generate"),
    path("names/favorites/", rpg_views.htmx_favorites, name="htmx_favorites"),
    path(
        "names/favorites/toggle/",
        rpg_views.htmx_toggle_favorite,
        name="htmx_toggle_favorite",
    ),
]
