from django import template

from sketches.models import Sketch

register = template.Library()


@register.inclusion_tag("sketches/includes/sketch.html")
def include_sketch(slug, width=800, height=600):
    """Render and start a compiled p5 sketch identified by its slug."""
    sketch = Sketch.objects.get(slug=slug)
    return {
        "sketch": sketch,
        "width": width,
        "height": height,
        "script_url": f"art/{sketch.slug}.js",
    }
