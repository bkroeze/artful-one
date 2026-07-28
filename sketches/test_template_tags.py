import pytest
from django.template import Context, Template

from sketches.models import Sketch


@pytest.mark.django_db
def test_include_sketch_renders_default_dimensions_and_autostart_scripts():
    Sketch.objects.create(name="Lotus", slug="lotus")

    rendered = Template("{% load sketch_tags %}{% include_sketch 'lotus' %}").render(
        Context()
    )

    assert 'id="lotus"' in rendered
    assert 'data-height="600"' in rendered
    assert 'data-width="800"' in rendered
    p5_script = "/static/js/p5/p5.min.js"
    sketch_script = "/static/art/lotus.js"
    assert p5_script in rendered
    assert sketch_script in rendered
    assert rendered.index(p5_script) < rendered.index(sketch_script)


@pytest.mark.django_db
def test_include_sketch_accepts_slug_and_dimensions_from_context():
    Sketch.objects.create(name="Lotus", slug="lotus")

    rendered = Template(
        "{% load sketch_tags %}{% include_sketch sketch_slug width=640 height=360 %}"
    ).render(Context({"sketch_slug": "lotus"}))

    assert 'id="lotus"' in rendered
    assert 'data-height="360"' in rendered
    assert 'data-width="640"' in rendered
