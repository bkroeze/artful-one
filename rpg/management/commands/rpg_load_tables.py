"""Load RPG tables from JSON files."""

import json
from pathlib import Path

from django.core.management.base import BaseCommand

from rpg.models import RpgTable, RpgTableAlias, TableVariant


class Command(BaseCommand):
    help = "Load RPG tables from JSON files into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--dir",
            type=str,
            default="rpg/json_import",
            help="Directory containing JSON table files (default: rpg/json_import)",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing tables and aliases before loading",
        )

    def handle(self, *args, **options):
        dir_path = Path(options["dir"])
        if not dir_path.exists():
            self.stdout.write(self.style.ERROR(f"Directory not found: {dir_path}"))
            return

        clear = options["clear"]

        if clear:
            self.stdout.write("Clearing existing tables and aliases...")
            count_tables = RpgTable.objects.count()
            count_aliases = RpgTableAlias.objects.count()
            RpgTableAlias.objects.all().delete()
            RpgTable.objects.all().delete()
            self.stdout.write(
                f"  Deleted {count_tables} tables and {count_aliases} aliases"
            )

        # Find all JSON files
        json_files = sorted(dir_path.glob("*.json"))
        if not json_files:
            self.stdout.write(self.style.WARNING(f"No JSON files found in {dir_path}"))
            return

        self.stdout.write(f"Found {len(json_files)} JSON file(s)")

        total_loaded = 0
        total_updated = 0

        for json_file in json_files:
            self.stdout.write(f"\nProcessing: {json_file.name}")
            try:
                with json_file.open("r", encoding="utf-8") as f:
                    tables_data = json.load(f)

                loaded, updated = self._load_tables(tables_data)
                total_loaded += loaded
                total_updated += updated

                self.stdout.write(
                    f"  Loaded {loaded} new tables, updated {updated} existing tables"
                )
            except json.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f"  Error parsing JSON: {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  Error loading file: {e}"))

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone! Total: {total_loaded} new, {total_updated} updated"
            )
        )

    def _load_tables(self, tables_data: list[dict]) -> tuple[int, int]:
        """Load tables from a list of table dictionaries.

        Returns:
            Tuple of (new_count, updated_count)
        """
        new_count = 0
        updated_count = 0

        for table_data in tables_data:
            slug = table_data.get("slug")
            if not slug:
                self.stdout.write("  Warning: Skipping table without slug")
                continue

            # Get or create the table
            try:
                table = RpgTable.objects.get(slug=slug)
                updated_count += 1
            except RpgTable.DoesNotExist:
                table = RpgTable(slug=slug)
                new_count += 1

            # Update table fields
            table.description = table_data.get("description", "") or slug
            table.variant = table_data.get("variant", "columns")
            table.delimiter = table_data.get("delimiter", "")
            table.hidden = table_data.get("hidden", False)
            table.data = table_data.get("table", [])
            table.addon = table_data.get("addon")

            # Validate variant
            if table.variant not in TableVariant.values:
                self.stdout.write(
                    f"  Warning: Unknown variant '{table.variant}' for {slug}"
                )
                table.variant = TableVariant.COLUMNS

            table.full_clean()
            table.save()

            # Create new aliases
            aliases = table_data.get("aliases", [])
            if not aliases:
                self.stdout.write(f"  Warning: Table {slug} has no aliases")

            for alias in aliases:
                try:
                    # Create new alias; if it exists but points to a different table,
                    # update it to point to this table (matches TS behavior where last one wins)
                    RpgTableAlias.objects.filter(alias=alias).delete()
                    RpgTableAlias.objects.create(alias=alias, table=table)
                except Exception as e:
                    self.stdout.write(
                        f"  Warning: Could not create alias '{alias}': {e}"
                    )

        return new_count, updated_count
