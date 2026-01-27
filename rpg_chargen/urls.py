"""URL configuration for RPG Character Generator app."""

from django.urls import path

from rpg_chargen import views as chargen_views

app_name = "rpg_chargen"

urlpatterns = [
    path("supers/", chargen_views.supers_page, name="supers"),
    path("supers/generate/", chargen_views.htmx_generate_names, name="generate_names"),
    path("supers/details/", chargen_views.htmx_generate_details, name="generate_details"),
    path("icons/", chargen_views.icons_page, name="icons"),
    path("icons/generate/", chargen_views.icons_htmx_generate, name="icons_generate"),
]
