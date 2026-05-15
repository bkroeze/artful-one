import pytest

from sketches.models import Animation, Sketch


@pytest.mark.django_db
def test_existing_sketch_listing_and_detail_routes_still_work(client):
    Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )

    listing = client.get("/sketch/")
    assert listing.status_code == 200
    assert "sketch_landing.html" in [template.name for template in listing.templates]
    assert "Orbit Study" in listing.content.decode()

    detail = client.get("/sketch/orbit-study/")
    assert detail.status_code == 200
    assert "sketch_detail.html" in [template.name for template in detail.templates]


@pytest.mark.django_db
def test_sketch_listing_only_lists_visible_sketches_by_default(client):
    Sketch.objects.create(
        name="Orbit Study",
        slug="orbit-study",
        description="Interactive orbit sketch",
    )
    Sketch.objects.create(
        name="Hidden Study",
        slug="hidden-study",
        description="Draft sketch",
        visible=False,
    )

    response = client.get("/sketch/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Orbit Study" in content
    assert "Hidden Study" not in content


@pytest.mark.django_db
def test_sketches_alias_remains_unrouted_because_it_was_not_present(client):
    response = client.get("/sketches/")

    assert response.status_code == 404


@pytest.mark.django_db
def test_animation_detail_route_renders_scorpion_partial(client):
    Animation.objects.get_or_create(
        slug="scorpion",
        defaults={"name": "Scorpion", "is_draft": False},
    )

    response = client.get("/animations/scorpion")

    assert response.status_code == 200
    assert "animation_detail.html" in [template.name for template in response.templates]
    assert "animations/scorpion.html" in [template.name for template in response.templates]
    content = response.content.decode()
    assert "Scorpion" in content
    assert 'id="scorpionStage"' in content
    assert "art/scorpion/scorpion.css" in content
    assert "art/scorpion/scorpion.js" in content
