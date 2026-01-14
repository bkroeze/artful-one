from django.db import models
from django.core.exceptions import ValidationError


class TableVariant(models.TextChoices):
    COLUMNS = "columns", "Columns"
    SELECT_ONE = "select-one", "Select One"
    ONE_FROM_EACH = "one-from-each", "One From Each"
    RANDOM_TABLE = "random-table", "Random Table"
    TEMPLATE = "template", "Template"


class RpgTable(models.Model):
    slug = models.CharField(
        max_length=255,
        unique=True,
        help_text="Internal canonical ID, e.g. names/2.1 or ad/ad1.1a",
    )
    description = models.TextField(help_text="Human-readable description of the table")
    variant = models.CharField(
        max_length=32,
        choices=TableVariant.choices,
        help_text="How the table data should be interpreted",
    )
    delimiter = models.CharField(
        max_length=32,
        default="",
        blank=True,
        help_text="Delimiter to join table columns",
    )
    hidden = models.BooleanField(
        default=False, help_text="Hide from public UI selectors"
    )
    data = models.JSONField(help_text="Table data as list of lists (rows x columns)")
    addon = models.JSONField(
        null=True,
        blank=True,
        help_text="Optional mapping of addon keys to table aliases, e.g. {'DEFAULT': '2.3', 'epithets': '2.3'}",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["slug"]
        verbose_name = "RPG Table"
        verbose_name_plural = "RPG Tables"

    def __str__(self):
        return f"{self.slug}: {self.description}"

    def clean(self):
        if self.variant == TableVariant.RANDOM_TABLE and not self.data:
            raise ValidationError("Random table variant requires at least one entry")
        if self.variant == TableVariant.ONE_FROM_EACH:
            if not self.data or not isinstance(self.data, list) or len(self.data) == 0:
                raise ValidationError(
                    "One-from-each variant requires a list of table aliases"
                )
            if not isinstance(self.data[0], list):
                raise ValidationError(
                    "One-from-each variant data must be a list of lists"
                )

    def get_addon_table(self, addon_key: str | None = None) -> str | None:
        """Get addon table alias for a given key, or DEFAULT if None."""
        if not self.addon:
            return None
        if addon_key is None:
            return self.addon.get("DEFAULT")
        return self.addon.get(addon_key, self.addon.get("DEFAULT"))


class RpgTableAlias(models.Model):
    alias = models.CharField(
        max_length=255, unique=True, help_text="Alias used to reference the table"
    )
    table = models.ForeignKey(
        RpgTable, on_delete=models.CASCADE, related_name="aliases"
    )

    class Meta:
        ordering = ["alias"]
        verbose_name = "RPG Table Alias"
        verbose_name_plural = "RPG Table Aliases"
        indexes = [
            models.Index(fields=["alias"]),
        ]

    def __str__(self):
        return f"{self.alias} -> {self.table.slug}"
