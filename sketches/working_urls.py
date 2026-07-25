from django.urls import path

from . import working_views

urlpatterns = [
    path(
        "api/sketches/",
        working_views.working_sketch_collection,
        name="working_sketch_collection",
    ),
    path(
        "api/sketches/<slug:slug>/",
        working_views.working_sketch_item,
        name="working_sketch_item",
    ),
    path(
        "api/media/",
        working_views.working_media_collection,
        name="working_media_collection",
    ),
    path(
        "api/media/<uuid:media_id>/",
        working_views.working_media_item,
        name="working_media_item",
    ),
    path(
        "media/<uuid:media_id>/<path:filename>",
        working_views.working_sketch_media,
        name="working_sketch_media",
    ),
    path(
        "sketches/<slug:slug>",
        working_views.working_sketch_detail,
        name="working_sketch_detail",
    ),
    path("sketches/<slug:slug>/", working_views.working_sketch_detail),
]
