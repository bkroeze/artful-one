"""Django admin configuration for sketches app."""

from django.contrib import admin, messages

from sketches.models import (
    Animation,
    Sketch,
    SketchToken,
    TemporarySketchMedia,
    WorkingSketch,
)


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


@admin.register(WorkingSketch)
class WorkingSketchAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "owner",
        "sketch_type",
        "updated_at",
    )
    list_filter = ("sketch_type", "created_at", "updated_at")
    search_fields = ("title", "slug", "owner__username")
    ordering = ("-updated_at",)
    autocomplete_fields = ("owner",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(SketchToken)
class SketchTokenAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "prefix",
        "active",
        "expires_at",
        "last_used_at",
        "created_at",
    )
    list_filter = ("active", "expires_at", "created_at", "last_used_at")
    search_fields = ("name", "prefix", "user__username", "user__email")
    ordering = ("user__username", "name")
    autocomplete_fields = ("user",)
    exclude = ("digest",)
    readonly_fields = ("prefix", "created_at", "updated_at", "last_used_at")

    def save_model(self, request, obj, form, change):
        if change:
            super().save_model(request, obj, form, change)
            return

        active = obj.active
        token, raw_token = SketchToken.issue(
            user=obj.user,
            name=obj.name,
            expires_at=obj.expires_at,
        )
        if token.active != active:
            token.active = active
            token.save(update_fields=("active", "updated_at"))
        obj.__dict__.update(token.__dict__)
        self.message_user(
            request,
            f"Copy this token now; it will not be shown again: {raw_token}",
            level=messages.SUCCESS,
        )


@admin.register(TemporarySketchMedia)
class TemporarySketchMediaAdmin(admin.ModelAdmin):
    list_display = (
        "original_name",
        "owner",
        "sketch",
        "content_type",
        "size",
        "created_at",
        "expires_at",
        "is_expired",
    )
    list_filter = ("content_type", "created_at", "expires_at")
    search_fields = (
        "original_name",
        "owner__username",
        "sketch__title",
        "sketch__slug",
    )
    ordering = ("-created_at",)
    autocomplete_fields = ("owner", "sketch")
    readonly_fields = ("id", "created_at", "reference", "is_expired")
