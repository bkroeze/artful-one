"""Table roller implementation for generating RPG names from tables."""

import random
import re
from typing import Optional


from rpg.models import RpgTable, RpgTableAlias, TableVariant


class TableResolver:
    """Resolve table aliases to RpgTable objects."""

    def __init__(self):
        self._cache = {}

    def flush_cache(self):
        """Clear the resolver cache."""
        self._cache.clear()

    def get_table(self, alias: str) -> Optional[RpgTable]:
        """Get table by alias, with caching."""
        if alias in self._cache:
            return self._cache[alias]

        table = None
        try:
            table_alias = RpgTableAlias.objects.select_related("table").get(alias=alias)
            table = table_alias.table
        except RpgTableAlias.DoesNotExist:
            pass

        if not table:
            try:
                table = RpgTable.objects.get(slug=alias)
            except RpgTable.DoesNotExist:
                pass

        if table:
            self._cache[alias] = table

        return table

    def resolve_template(self, template: str, max_depth: int = 10) -> str:
        """Resolve a template string by expanding [table-alias] patterns.

        Supports pipe-delimited alternatives: [alias1|alias2|alias3]
        Recursive expansion is supported up to max_depth.
        """
        if max_depth <= 0:
            return template

        # Find all bracket patterns
        pattern = r"\[([^\]]+)\]"

        def replace_match(match):
            content = match.group(1)
            if not content.strip():
                return match.group(0)  # Return original if empty

            # Split by pipe to get alternatives
            alternatives = [a.strip() for a in content.split("|") if a.strip()]
            if not alternatives:
                return match.group(0)

            # Pick random alternative
            chosen = random.choice(alternatives)
            table = self.get_table(chosen)
            if not table:
                return match.group(0)  # Return original if table not found

            name = make_name(table, move_gt=True)
            # Recursively expand further if needed
            if "[" in name and "]" in name:
                name = self.resolve_template(name, max_depth - 1)

            return name

        # Replace all patterns
        result = re.sub(pattern, replace_match, template)
        return result


_resolver = TableResolver()


def roll_dice(size: int) -> int:
    """Roll a dice with 'size' faces (0 to size-1)."""
    if size <= 0:
        return 0
    return random.randint(0, size - 1)


def move_gt_to_end(name: str) -> str:
    """Move words delimited with |> to the end of the word.

    Examples:
        |forest> gold -> gold forest
        a |gold forest> big -> a big gold forest
    """
    if not name:
        return name

    parts = name.split(">")
    if len(parts) == 1:
        return name

    last_parts = []
    out_parts = []

    for part in parts:
        if "|" in part:
            sub_parts = part.split("|")
            if len(sub_parts) >= 1:
                out_parts.append(sub_parts[0])
            if len(sub_parts) >= 2:
                last_parts.append(sub_parts[1])
        else:
            out_parts.append(part)

    result = f"{''.join(out_parts)} {''.join(last_parts)}".strip()
    return result


def make_name(table: RpgTable, move_gt: bool = False) -> str:
    """Generate a name from a table based on its variant."""
    if not table or not table.data:
        return ""

    variant = table.variant
    delimiter = table.delimiter or ""

    if variant == TableVariant.COLUMNS:
        # columns: pick one random row, concatenate columns
        roll_size = len(table.data)
        if roll_size == 0:
            return ""

        roll = roll_dice(roll_size)
        row = table.data[roll]
        if not isinstance(row, list):
            return str(row)

        parts = [str(item) for item in row]
        name = delimiter.join(parts)

    elif variant == TableVariant.SELECT_ONE:
        # select-one: pick random cell from the table
        roll_size = len(table.data)
        if roll_size == 0:
            return ""

        # Find number of columns from first row
        first_row = table.data[0]
        if not isinstance(first_row, list):
            cols = 1
        else:
            cols = len(first_row)

        col_roll = roll_dice(cols)
        row_roll = roll_dice(roll_size)

        row = table.data[row_roll]
        if isinstance(row, list):
            name = str(row[col_roll])
        else:
            name = str(row)

    elif variant == TableVariant.ONE_FROM_EACH:
        # one-from-each: resolve each sub-table alias and concatenate
        if not table.data or not isinstance(table.data, list):
            return ""

        parts = []
        sub_aliases = table.data[0] if table.data else []

        for sub_alias in sub_aliases:
            if not sub_alias:
                continue
            if isinstance(sub_alias, list):
                sub_alias = sub_alias[0] if sub_alias else ""

            sub_table = _resolver.get_table(str(sub_alias))
            if sub_table:
                parts.append(make_name(sub_table))

        name = delimiter.join(parts)

    elif variant == TableVariant.RANDOM_TABLE:
        # random-table: pick a random table alias and generate from it
        roll_size = len(table.data)
        if roll_size == 0:
            return ""

        roll = roll_dice(roll_size)
        sub_alias = table.data[roll]
        if isinstance(sub_alias, list):
            sub_alias = sub_alias[0] if sub_alias else ""

        sub_table = _resolver.get_table(str(sub_alias))
        if sub_table:
            name = make_name(sub_table)
        else:
            name = ""

    elif variant == TableVariant.TEMPLATE:
        # template: pick a random template and expand it
        roll_size = len(table.data)
        if roll_size == 0:
            return ""

        roll = roll_dice(roll_size)
        template = table.data[roll]
        if isinstance(template, list):
            template = template[0] if template else ""

        name = _resolver.resolve_template(str(template))
    else:
        name = ""

    # Fix "- " to "-"
    name = name.replace("- ", "-")

    # Move |> segments to end if requested
    if move_gt:
        name = move_gt_to_end(name)

    # Handle nested templates
    if "[" in name and "]" in name:
        name = _resolver.resolve_template(name)

    return name


def generate(
    alias_or_template: str,
    count: int = 1,
    addon_key: Optional[str] = None,
    allow_template: bool = True,
) -> list[str]:
    """Generate names from a table alias or template.

    Args:
        alias_or_template: Table alias or template string (e.g., "2.1" or "[2.1-a|2.1-b]")
        count: Number of names to generate
        addon_key: Optional addon key to append (e.g., "epithets", "forest", etc.)
        allow_template: If True, treat bracket patterns as templates (not raw output)

    Returns:
        List of generated names
    """
    names = []

    for _ in range(count):
        # Check if this is a template (contains brackets)
        if allow_template and "[" in alias_or_template and "]" in alias_or_template:
            name = _resolver.resolve_template(alias_or_template)
            name = move_gt_to_end(name)
        else:
            # Look up table by alias
            table = _resolver.get_table(alias_or_template)
            if not table:
                name = f"[Unknown table: {alias_or_template}]"
            else:
                name = make_name(table, move_gt=True)

                # Handle addons
                addon_alias = None
                if table.addon:
                    if addon_key is None:
                        addon_alias = table.addon.get("DEFAULT")
                    elif addon_key in table.addon:
                        addon_alias = table.addon[addon_key]
                    elif "DEFAULT" in table.addon:
                        addon_alias = table.addon["DEFAULT"]

                if addon_alias:
                    addon_table = _resolver.get_table(addon_alias)
                    if addon_table:
                        addon_name = make_name(addon_table)
                        addon_delimiter = addon_table.delimiter or ""
                        name = f"{name}{addon_delimiter}{addon_name}"

        names.append(name)

    return names


def get_resolver() -> TableResolver:
    """Get the global table resolver instance."""
    return _resolver


def flush_resolver_cache():
    """Clear the resolver cache."""
    _resolver.flush_cache()
