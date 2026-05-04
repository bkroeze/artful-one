import pytest


@pytest.mark.django_db
def test_primary_navigation_has_art_but_not_sketches(client):
    response = client.get("/")

    assert response.status_code == 200
    content = response.content.decode()

    assert content.count('<a class="item" href="/art/">Art</a>') == 3
    assert 'href="/sketch/">Sketches</a>' not in content
