"""Custom template filters for RPG app."""

import json

from django import template

register = template.Library()


@register.filter
def to_json(value):
    """Convert a Python object to a JSON-safe string for use in HTML attributes.

    This can be used to safely embed JSON in data attributes like:
        <option data-value="{{ table.addon|to_json }}">
    """
    if value is None:
        return ""
    return json.dumps(value)
