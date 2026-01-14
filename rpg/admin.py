"""Django admin configuration for RPG app."""

from django.contrib import admin

from rpg.models import RpgTable, RpgTableAlias


@admin.register(RpgTableAlias)
class RpgTableAliasAdmin(admin.ModelAdmin):
    list_display = ("alias", "table")
    list_filter = ("table",)
    search_fields = ("alias",)
    raw_id_fields = ("table",)


class RpgTableAliasInline(admin.TabularInline):
    model = RpgTableAlias
    extra = 0
    fields = ("alias",)


@admin.register(RpgTable)
class RpgTableAdmin(admin.ModelAdmin):
    list_display = ("slug", "description", "variant", "hidden")
    list_filter = ("variant", "hidden")
    search_fields = ("slug", "description")
    ordering = ("slug",)

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": ("slug", "description", "hidden"),
            },
        ),
        (
            "Table Configuration",
            {
                "fields": ("variant", "delimiter", "data"),
            },
        ),
        (
            "Addon Tables",
            {
                "fields": ("addon",),
                "description": "Optional mapping of addon keys to table aliases",
            },
        ),
    )

    inlines = [RpgTableAliasInline]
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("aliases")
