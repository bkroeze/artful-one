import pytest

from blog.models import Photo, PhotoTag
from sketches.models import Animation, Sketch


@pytest.mark.django_db
def test_art_landing_renders_sketches_and_galleries(client):
    animation = Animation.objects.get(slug="scorpion")
    sketch = Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )
    photo_tag = PhotoTag.objects.create(slug="paintings", name="Paintings")
    photo = Photo.objects.create(title="Blue Field", slug="blue-field")
    photo.photo_tags.add(photo_tag)

    response = client.get("/art/")

    assert response.status_code == 200
    assert list(response.context["animations"]) == [animation]
    assert list(response.context["sketches"]) == [sketch]
    assert response.context["total_photos"] == 1

    content = response.content.decode()
    assert "Live Animations" in content
    assert "Galleries" in content
    assert "Scorpion" in content
    assert "/animations/scorpion" in content
    assert "Orbit Study" in content
    assert "/sketch/orbit-study/" in content
    assert content.index("Scorpion") < content.index("Orbit Study")
    assert "Paintings" in content
    assert "/photo-tags/paintings/" in content


@pytest.mark.django_db
def test_art_landing_shows_galleries_with_no_sketches(client):
    photo_tag = PhotoTag.objects.create(slug="paintings", name="Paintings")
    photo = Photo.objects.create(title="Blue Field", slug="blue-field")
    photo.photo_tags.add(photo_tag)

    response = client.get("/art/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Live Animations" in content
    assert "Galleries" in content
    assert "Scorpion" in content
    assert "No sketches found." not in content
    assert "No photo collections found." not in content
    assert "Paintings" in content
    assert "/photo-tags/paintings/" in content


@pytest.mark.django_db
def test_art_landing_shows_sketches_with_no_galleries(client):
    Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )

    response = client.get("/art/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Live Animations" in content
    assert "Galleries" in content
    assert "No photo collections found." in content
    assert "No sketches found." not in content
    assert "Orbit Study" in content
    assert "/sketch/orbit-study/" in content


@pytest.mark.django_db
def test_art_landing_only_lists_visible_sketches_by_default(client):
    visible_sketch = Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )
    hidden_sketch = Sketch.objects.create(
        name="Hidden Study",
        slug="hidden-study",
        description="Draft sketch",
        visible=False,
    )

    response = client.get("/art/")

    assert response.status_code == 200
    assert list(response.context["sketches"]) == [visible_sketch]
    content = response.content.decode()
    assert "Orbit Study" in content
    assert "Hidden Study" not in content
    assert hidden_sketch.visible is False


@pytest.mark.django_db
def test_art_landing_only_lists_non_draft_animations(client):
    visible_animation = Animation.objects.get(slug="scorpion")
    draft_animation = Animation.objects.create(
        name="Private Animation",
        slug="private-animation",
        is_draft=True,
    )

    response = client.get("/art/")

    assert response.status_code == 200
    assert list(response.context["animations"]) == [visible_animation]
    content = response.content.decode()
    assert "Scorpion" in content
    assert "/animations/scorpion" in content
    assert "Private Animation" not in content
    assert draft_animation.is_draft is True


@pytest.mark.django_db
def test_art_landing_only_lists_animations_with_templates(client):
    visible_animation = Animation.objects.get(slug="scorpion")
    missing_template_animation = Animation.objects.create(
        name="Missing Template",
        slug="missing-template",
        is_draft=False,
    )

    response = client.get("/art/")

    assert response.status_code == 200
    assert list(response.context["animations"]) == [visible_animation]
    content = response.content.decode()
    assert "Scorpion" in content
    assert "Missing Template" not in content
    assert missing_template_animation.has_template() is False


@pytest.mark.django_db
def test_animation_detail_404s_for_draft_animation(client):
    Animation.objects.create(
        name="Private Animation",
        slug="private-animation",
        is_draft=True,
    )

    response = client.get("/animations/private-animation")

    assert response.status_code == 404


@pytest.mark.django_db
def test_animation_detail_404s_for_missing_template(client):
    Animation.objects.create(
        name="Missing Template",
        slug="missing-template",
        is_draft=False,
    )

    response = client.get("/animations/missing-template")

    assert response.status_code == 404
