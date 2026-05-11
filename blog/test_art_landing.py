import pytest

from blog.models import Photo, PhotoTag
from sketches.models import Sketch


@pytest.mark.django_db
def test_art_landing_renders_sketches_and_galleries(client):
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
    assert list(response.context["sketches"]) == [sketch]
    assert response.context["total_photos"] == 1

    content = response.content.decode()
    assert "Live Art Code" in content
    assert "Galleries" in content
    assert "Orbit Study" in content
    assert '/sketch/orbit-study/' in content
    assert "Paintings" in content
    assert '/photo-tags/paintings/' in content


@pytest.mark.django_db
def test_art_landing_shows_galleries_with_no_sketches(client):
    photo_tag = PhotoTag.objects.create(slug="paintings", name="Paintings")
    photo = Photo.objects.create(title="Blue Field", slug="blue-field")
    photo.photo_tags.add(photo_tag)

    response = client.get("/art/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Live Art Code" in content
    assert "Galleries" in content
    assert "No sketches found." in content
    assert "No photo collections found." not in content
    assert "Paintings" in content
    assert '/photo-tags/paintings/' in content


@pytest.mark.django_db
def test_art_landing_shows_sketches_with_no_galleries(client):
    sketch = Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )

    response = client.get("/art/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Live Art Code" in content
    assert "Galleries" in content
    assert "No photo collections found." in content
    assert "No sketches found." not in content
    assert "Orbit Study" in content
    assert '/sketch/orbit-study/' in content


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
