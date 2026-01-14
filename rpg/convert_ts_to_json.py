#!/usr/bin/env python3
"""Convert TypeScript table files to JSON for import into Django."""

import json
import re
from pathlib import Path


def parse_ts_array_variable(content: str, var_name: str) -> list[dict]:
    """
    Parse a TypeScript array variable from content.
    Expects format: export const VAR: Array<Type> = [ ... ];
    """
    # Find the variable declaration
    pattern = rf"export const {var_name}: Array<[^>]+>\s*=\s*(\[.*?\]);"
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        raise ValueError(f"Could not find variable '{var_name}' in content")

    array_str = match.group(1)

    # Clean comments (simple removal) - but preserve content within strings
    result = []
    in_string = False
    string_char = None

    for char in array_str:
        if char in ('"', "'") and (not in_string or char == string_char):
            if in_string and char == string_char:
                # Check if escaped
                if result and result[-1] != "\\":
                    in_string = False
                    string_char = None
                # else: escaped quote, stay in string
            else:
                in_string = True
                string_char = char
            result.append(char)
        elif in_string:
            result.append(char)
        elif char == "/" and len(result) > 0 and result[-1] == "/" and not in_string:
            # Remove the previous slash (start of comment) and skip until newline
            if result:
                result.pop()  # Remove the first /
                # Skip characters until newline
            continue
        elif char == "\n":
            result.append(char)
            in_string = False  # Comment ends at newline
            string_char = None
        else:
            result.append(char)

    array_str = "".join(result)

    # Remove trailing commas before closing brackets/braces
    array_str = re.sub(r",(\s*[}\]])", r"\1", array_str)

    # TypeScript uses unquoted keys - quote them but respect strings
    # Use a state machine approach to only quote keys outside strings
    result_chars = []
    in_string = False
    string_char = None
    i = 0

    while i < len(array_str):
        char = array_str[i]

        # Track string literals
        if char in ('"', "'") and (not in_string or char == string_char):
            if (
                in_string
                and char == string_char
                and (i == 0 or array_str[i - 1] != "\\")
            ):
                in_string = False
                string_char = None
            elif not in_string:
                in_string = True
                string_char = char
            result_chars.append(char)
            i += 1
            continue

        if in_string:
            result_chars.append(char)
            i += 1
            continue

        # Outside strings: look for unquoted keys followed by colon
        # Pattern: whitespace, word, whitespace, colon
        if char.isalpha() or char == "_":
            # Check if this is a key followed by colon
            start = i
            while i < len(array_str) and (
                array_str[i].isalnum() or array_str[i] in ("_", "-")
            ):
                i += 1
            word = array_str[start:i]
            # Skip whitespace
            while i < len(array_str) and array_str[i] in " \t":
                i += 1
            # Check if next char is colon
            if i < len(array_str) and array_str[i] == ":":
                # Also check if there's already quotes before this word
                # Look back for non-whitespace before the word
                j = start - 1
                while j >= 0 and array_str[j] in " \t":
                    j -= 1
                if j < 0 or array_str[j] not in ('"', "'"):
                    # This is an unquoted key, quote it
                    result_chars.append(f'"{word}"')
                else:
                    result_chars.append(word)
            else:
                result_chars.append(word)
            continue

        result_chars.append(char)
        i += 1

    array_str = "".join(result_chars)

    try:
        data = json.loads(array_str)
        return data
    except json.JSONDecodeError as e:
        # If that fails, try eval as Python literal (for trusted input)
        try:
            import ast

            return ast.literal_eval(array_str)
        except Exception as e2:
            raise ValueError(f"Failed to parse array: {e} / {e2}")


def convert_tables_to_json(ts_file: Path, json_file: Path, source_type: str):
    """Convert a TypeScript table file to JSON."""
    print(f"Converting {ts_file} -> {json_file}")

    content = ts_file.read_text()

    # Determine which variable to parse based on file/source
    if source_type == "names":
        var_name = "TABLES"
        slug_prefix = "names"
    elif source_type == "adventure-design":
        var_name = "ADVENTURE_DESIGN_TABLES"
        slug_prefix = "ad"
    else:
        raise ValueError(f"Unknown source type: {source_type}")

    tables = parse_ts_array_variable(content, var_name)

    # Process tables: add slugs and clean data
    output_tables = []
    for table in tables:
        if not table:
            continue

        # Create a slug from the first non-hidden alias
        aliases = table.get("aliases", [])
        if not aliases:
            print(
                f"Warning: Table has no aliases, skipping: {table.get('description', 'Unknown')}"
            )
            continue

        # Use the first alias as the base for slug
        primary_alias = aliases[0]
        slug = f"{slug_prefix}/{primary_alias}"

        output_table = {
            "slug": slug,
            "aliases": aliases,
            "description": table.get("description", ""),
            "variant": table.get("variant", "columns"),
            "delimiter": table.get("delimiter", ""),
            "table": table.get("table", []),
            "hidden": table.get("hidden", False),
        }

        if "addon" in table and table["addon"]:
            output_table["addon"] = table["addon"]

        output_tables.append(output_table)

    # Write to JSON file
    json_file.write_text(json.dumps(output_tables, indent=2, ensure_ascii=False) + "\n")

    print(f"  -> Converted {len(output_tables)} tables")
    return output_tables


def main():
    """Main conversion script."""
    base_dir = Path(__file__).parent.parent
    tmp_dir = base_dir / "tmp"
    json_import_dir = base_dir / "rpg" / "json_import"

    # Ensure output directory exists
    json_import_dir.mkdir(parents=True, exist_ok=True)

    # Convert names.ts
    names_ts = tmp_dir / "names.ts"
    names_json = json_import_dir / "names.json"

    if names_ts.exists():
        convert_tables_to_json(names_ts, names_json, "names")
    else:
        print(f"Warning: {names_ts} not found, skipping")

    # Convert adventure-design.ts
    adventure_ts = tmp_dir / "adventure-design.ts"
    adventure_json = json_import_dir / "adventure-design.json"

    if adventure_ts.exists():
        convert_tables_to_json(adventure_ts, adventure_json, "adventure-design")
    else:
        print(f"Warning: {adventure_ts} not found, skipping")

    print("\nConversion complete!")


if __name__ == "__main__":
    main()
