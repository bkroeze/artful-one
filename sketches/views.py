from django.http import Http404
from django.shortcuts import get_object_or_404, render
import logging

from .models import Animation, Sketch

log = logging.getLogger(__name__)


def sketch_landing(request):
    """Display landing page listing all P5 sketches."""
    if Sketch is None:
        return render(request, "no_sketches.html")

    sketches = Sketch.objects.filter(visible=True).order_by("name")
    return render(request, "sketch_landing.html", {"sketches": sketches})


def sketch_detail(request, slug):
    """Display detail page for a single P5 sketch."""
    if Sketch is None:
        return render(request, "no_sketches.html")

    sketch = get_object_or_404(Sketch, slug=slug)
    return render(
        request,
        "sketch_detail.html",
        {
            "sketch": sketch,
            "script_url": f"art/{sketch.slug}.js",
        },
    )


def animation_detail(request, slug):
    """Display detail page for a single animation."""
    animation = get_object_or_404(Animation, slug=slug, is_draft=False)
    if not animation.has_template():
        raise Http404("Animation template not found")
    return render(
        request,
        "animation_detail.html",
        {
            "animation": animation,
            "animation_template": animation.template_name,
        },
    )
