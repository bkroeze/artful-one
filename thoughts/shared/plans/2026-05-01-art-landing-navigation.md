# Art Landing Navigation Implementation Plan

**Goal:** Replace the split Art/Sketches top-level navigation with one `/art/` landing page that presents both live code sketches and photo galleries while preserving existing sketch URLs.

**Architecture:** Keep the current `/art/` route (`blog.views.photo_tag_landing`) as the unified landing endpoint, and extend its context with the existing `Sketch` queryset. Reuse the current sketch card markup and photo-tag gallery card markup in `templates/photo_tag_landing.html`, with independent empty states for both sections. Keep `path("sketch/", include("sketches.urls"))` unchanged; because `/sketches/` is not currently routed, do not add a new alias.

**Design:** `thoughts/shared/designs/2026-05-01-art-landing-navigation-design.md`

**Pattern lookup:** `.mindmodel/` is absent in this repository, so implementation follows existing Django/pytest/template conventions observed in `templates/site_page.html`, `blog/views.py`, `sketches/views.py`, `templates/photo_tag_landing.html`, and `sketches/templates/sketch_landing.html`.

---

## Dependency Graph

```text
Batch 1 (parallel): 1.1, 1.2 [tests first - no deps]
Batch 2 (parallel): 2.1, 2.2 [implementation - depends on matching tests]
Batch 3 (parallel): 3.1 [compatibility regression tests - depends on implementation remaining stable]
```

---

## Batch 1: Failing Tests (parallel - 2 implementers)

### Task 1.1: Primary navigation regression tests
**File:** `blog/test_art_navigation.py`
**Test:** same file
**Depends:** none

Design requires one primary Art link and no Sketches primary nav entry. Implementing this as a rendered homepage/nav regression because `templates/site_page.html` contains the fixed, sidebar, and masthead menu variants.

```python
import pytest


@pytest.mark.django_db
def test_primary_navigation_has_art_but_not_sketches(client):
    response = client.get("/")

    assert response.status_code == 200
    content = response.content.decode()

    assert content.count('<a class="item" href="/art/">Art</a>') == 3
    assert 'href="/sketch/">Sketches</a>' not in content
```

**Verify fail before implementation:** `uv run pytest blog/test_art_navigation.py`
**Commit:** `test(nav): cover unified art navigation`

### Task 1.2: Unified `/art/` landing tests
**File:** `blog/test_art_landing.py`
**Test:** same file
**Depends:** none

Design requires `/art/` to render both “Live Art Code” and “Galleries” using existing content streams. Implementing tests with one `Sketch`, one `PhotoTag`, and one `Photo` without image data so the card/link behavior is tested without fixture files.

```python
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
    assert "photo_tag_landing.html" in [template.name for template in response.templates]
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
def test_art_landing_preserves_independent_empty_states(client):
    response = client.get("/art/")

    assert response.status_code == 200
    content = response.content.decode()
    assert "Live Art Code" in content
    assert "Galleries" in content
    assert "No sketches found." in content
    assert "No photo collections found." in content
```

**Verify fail before implementation:** `uv run pytest blog/test_art_landing.py`
**Commit:** `test(art): cover unified art landing`

---

## Batch 2: Implementation (parallel where possible - 2 implementers)

### Task 2.1: Remove Sketches from primary navigation
**File:** `templates/site_page.html`
**Test:** `blog/test_art_navigation.py`
**Depends:** 1.1

Remove these three lines only; leave the Art links pointing to `/art/` in fixed, sidebar, and masthead variants:

```django
<a class="item" href="/sketch/">Sketches</a>
```

Expected complete result for the relevant nav groups:

```django
<a class="item" href="/">Artful.One</a>
<a class="item" href="/about/">About</a>
<a class="item" href="/art/">Art</a>
```

Apply this in all three existing locations: lines currently equivalent to `13`, `29`, and `52` in `templates/site_page.html`.

**Verify:** `uv run pytest blog/test_art_navigation.py`
**Commit:** `fix(nav): remove sketches primary link`

### Task 2.2: Feed sketches into the existing `/art/` view
**File:** `blog/views.py`
**Test:** `blog/test_art_landing.py`
**Depends:** 1.2

Replace the existing `photo_tag_landing()` function with this complete implementation. This keeps the route name/view stable but adds `sketches` to the context for the unified landing page.

```python
def photo_tag_landing(request):
    """Display unified art landing page with live code sketches and photo galleries."""
    from django.db.models import Count
    from sketches.models import Sketch

    photo_tags = (
        PhotoTag.objects.annotate(photo_count=Count("photo"))
        .filter(photo_count__gt=0)
        .order_by("name")
    )

    tag_data = []
    total_photos = 0
    for photo_tag in photo_tags:
        photos = Photo.objects.filter(photo_tags=photo_tag)
        photo_count = photos.count()
        total_photos += photo_count

        if photo_count > 0:
            random_photo = photos.order_by("?").first()
            tag_data.append(
                {
                    "tag": photo_tag,
                    "photo": random_photo,
                    "photo_count": photo_count,
                }
            )

    sketches = Sketch.objects.select_related("photo").all().order_by("name")

    return render(
        request,
        "photo_tag_landing.html",
        {
            "sketches": sketches,
            "tag_data": tag_data,
            "total_photos": total_photos,
        },
    )
```

**Verify:** `uv run pytest blog/test_art_landing.py`
**Commit:** `feat(art): include sketches on art landing`

---

## Batch 3: Template + Compatibility Regression (parallel-safe after Batch 2)

### Task 3.1: Convert gallery template into unified art landing template
**File:** `templates/photo_tag_landing.html`
**Test:** `blog/test_art_landing.py`
**Depends:** 2.2

Replace the full file with this complete template. It intentionally reuses the existing `sketches-grid` / `sketch-card` markup from `sketch_landing.html` and the existing `photo-tags-grid` / `tag-card` gallery markup from `photo_tag_landing.html`.

```django
{% extends "site_detail_page.html" %}{% load humanize %}

{% load pictures %}
{% load blog_tags %}

{% block title %}Art - Bruce Kroeze{% endblock %}

{% block extrahead %}
<meta property="og:type" content="website" />
<meta property="og:title" content="Art - Bruce Kroeze" />
<meta property="og:description" content="Live art code and photo galleries by Bruce Kroeze." />
<meta property="og:site_name" content="Bruce Kroeze's Weblog" />
<style>
.art-section {
    margin-bottom: 3rem;
}

.art-section-header {
    margin-top: 2rem;
}

.sketches-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
}

.sketch-card {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    text-decoration: none;
    color: inherit;
    transition: transform 0.2s ease;
}

.sketch-card:hover {
    transform: translateY(-4px);
}

.sketch-card .ui.card,
.tag-card .ui.card {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.sketch-card .ui.card .content,
.tag-card .ui.card .content {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.sketch-card .ui.card .image {
    height: 300px;
    overflow: hidden;
}

.photo-tags-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.tag-card {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    text-decoration: none;
    color: inherit;
}

.tag-card:hover .ui.card {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
    transition: all 0.2s ease;
}

.tag-card .ui.card .image {
    height: 250px;
    overflow: hidden;
}

.sketch-card .ui.card .image img,
.tag-card .ui.card .image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
{% endblock %}

{% block primary %}
<h1 class="archive-h2">Art</h1>
<p class="text-muted">
    Browse live generative art sketches and photo galleries.
</p>

<section class="art-section" aria-labelledby="live-art-code-heading">
    <h2 id="live-art-code-heading" class="archive-h2 art-section-header">Live Art Code</h2>
    <p class="text-muted">
        Browse {{ sketches|length }} interactive sketch{{ sketches|pluralize }} created with P5.js.
    </p>

    {% if sketches %}
    <div class="sketches-grid">
        {% for sketch in sketches %}
        <a href="{% url 'sketch_detail' slug=sketch.slug %}" class="sketch-card">
            <div class="ui card">
                {% if sketch.photo and sketch.photo.image %}
                <div class="image">
                    {% picture sketch.photo.image picture_id=sketch.photo.html_id img_alt=sketch.title|default:"Sketch" img_loading="lazy" picture_class="ui fluid image" %}
                </div>
                {% endif %}
                <div class="content">
                    <div class="header">{{ sketch.name }}</div>
                    {% if sketch.description %}
                    <div class="description">
                        {{ sketch.description|truncatewords:20 }}
                    </div>
                    {% endif %}
                    <div class="meta">
                        <span class="date">Created {{ sketch.created_at|date:"F j, Y" }}</span>
                    </div>
                </div>
            </div>
        </a>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-muted">No sketches found.</p>
    {% endif %}
</section>

<section class="art-section" aria-labelledby="galleries-heading">
    <h2 id="galleries-heading" class="archive-h2 art-section-header">Galleries</h2>
    <p class="text-muted">
        Browse {{ tag_data|length }} photo collection{{ tag_data|pluralize }}.
    </p>

    {% if tag_data %}
    <div class="photo-tags-grid">
        {% for item in tag_data %}
        <a href="/photo-tags/{{ item.tag.slug }}/" class="tag-card">
            <div class="ui card">
                {% if item.photo.image %}
                <div class="image">
                    {% picture item.photo.image picture_id=item.photo.html_id img_alt=item.photo.title|default:"Photo" img_loading="lazy" picture_class="ui fluid image" %}
                </div>
                {% endif %}
                <div class="content">
                    <div class="header">{{ item.tag.name }}</div>
                    {% if item.photo.title %}
                    <div class="description">
                        <em>{{ item.photo.title }}</em>
                    </div>
                    {% endif %}
                    <div class="meta">
                        <span class="date">
                            {{ item.photo_count }} photo{{ item.photo_count|pluralize }}
                        </span>
                    </div>
                </div>
            </div>
        </a>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-muted">No photo collections found.</p>
    {% endif %}
</section>
{% endblock %}

{% block secondary %}
<div class="ui container" style="margin-top: 2rem;">
    <p><strong>Live Art Code</strong></p>
    <p>Click on any sketch to view the P5.js canvas.</p>
    <p>{{ sketches|length }} sketch{{ sketches|pluralize }}</p>

    <p><strong>Galleries</strong></p>
    <p>Click on any collection to view all photos tagged with that theme.</p>
    <p>{{ tag_data|length }} collection{{ tag_data|pluralize }}</p>

    <p><strong>Total Photos</strong></p>
    <p>{{ total_photos|intcomma }}</p>
</div>
{% endblock %}
```

**Verify:** `uv run pytest blog/test_art_landing.py`
**Commit:** `feat(art): compose unified art landing template`

### Task 3.2: Preserve sketch route compatibility with explicit tests
**File:** `blog/test_sketch_compatibility.py`
**Test:** same file
**Depends:** 2.1, 2.2, 3.1

Design requires existing sketch URLs to remain compatible. Implementing `/sketch/` and per-sketch detail assertions, and documenting that `/sketches/` remains unrouted because it is not currently present.

```python
import pytest

from sketches.models import Sketch


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
def test_sketches_alias_remains_unrouted_because_it_was_not_present(client):
    response = client.get("/sketches/")

    assert response.status_code == 404
```

**Verify:** `uv run pytest blog/test_sketch_compatibility.py`
**Commit:** `test(sketches): preserve direct route compatibility`

---

## Final Verification

Run the focused tests first:

```bash
uv run pytest blog/test_art_navigation.py blog/test_art_landing.py blog/test_sketch_compatibility.py
```

Then run the repository test suite:

```bash
uv run pytest
```

Manual browser smoke checks after implementation:

- `/art/` shows one page with “Live Art Code” above “Galleries”.
- `/sketch/` still shows the original sketch listing.
- `/sketch/<slug>/` still opens the existing sketch detail page.
- Primary navigation shows Art but not Sketches in fixed, sidebar, and masthead menus.
