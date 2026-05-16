"""Django admin configuration for sketches app."""

from django.contrib import admin

from sketches.models import Animation, Sketch


@admin.register(Sketch)
class SketchAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "visible", "created_at")
    list_filter = ("visible", "created_at")
    search_fields = ("name", "slug", "description")
    ordering = ("name",)


@admin.register(Animation)
class AnimationAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_draft", "created_at")
    list_filter = ("is_draft", "created_at")
    search_fields = ("name", "slug")
    ordering = ("name",)
    autocomplete_fields = ("thumbnail",)
