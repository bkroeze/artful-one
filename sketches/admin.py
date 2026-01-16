"""Django admin configuration for sketches app."""

from django.contrib import admin

from sketches.models import Sketch


@admin.register(Sketch)
class SketchAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "slug", "description")
    ordering = ("name",)
