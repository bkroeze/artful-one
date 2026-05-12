# Architecture Guide

## Purpose

Artful.One is a Django personal blog site. It manages multiple content types (entries, blogmarks, quotations, notes), supports tagging, search, and syndicated feeds, and publishes readable URLs and archived content.

## Repository Layout

- `config/` — Django settings and URL hosts:
  - `settings.py`
  - `urls.py` (including django-hosts support)
  - `hosts.py`
  - `wsgi.py`
- `blog/` — Core models, views, feeds, templates context, and content behavior.
- `monthly/` — Monthly archive app.
- `feedstats/` — Feed subscriber tracking and analytics.
- `pixelborders/` — Authenticated pixel border editor, saved border designs, generated CSS, and AI-assisted frame generation.
- `templates/` — Shared and app templates.
- `static/` — Source assets.
- `staticfiles/` — Collected/static build output.
- `photos/` — Image/media storage (`.jpg`, `.avif`, etc.).
- `README.md` — onboarding documentation.

## Data Model Conventions

Content models under `blog/` inherit from `BaseModel`, which centralizes common fields:

- `created` (`DateTimeField`)
- `tags` (`ManyToMany` to `Tag`)
- `slug`
- `metadata` (`JSONField`)
- `import_ref`
- `card_image`
- `series`
- `is_draft`

Model types:

- `Entry`: standard post with title/body and optional custom template.
- `Blogmark`: link + title + URL + commentary.
- `Quotation`: quote + source + optional context.
- `Note`: short-form, optional title.

## URL Conventions

- Canonical date URL: `/{YYYY}/{Mon}/{D}/{slug}/` (for example `/2024/Oct/15/my-blog-post/`).
- Short aliases for quick access: `/e/{id}/`, `/b/{id}/`, `/q/{id}/`, `/n/{id}/`.
- Pixel border editor routes live under `/borders/`.

## Pixel Borders

`pixelborders/` owns `PixelBorderDesign`, editor views, HTMX fragments, and CSS export for saved border-image frames.

- Designs are owner-scoped, may be public, and store dimensions, repeat mode, palette, and pixel grid JSON.
- CSS is generated from saved designs as `border-image` rules with embedded PNG data URLs for export/use elsewhere.
- AI frame generation is centralized in `pixelborders.ai.generate_frame()`.

## Contact Form

The site-level `/contact/` route is handled by `blog.views.contact`.

- Submissions are validated by `ContactMessageForm` and persisted as `ContactMessage` records before email delivery.
- HTMX requests render `templates/includes/contact_form.html`; full-page requests render `templates/contact.html`.
- Mailgun delivery uses `MAILGUN_API_KEY`, `MAILGUN_DOMAIN`, `MAILGUN_API_URL`, `MAILGUN_FROM_EMAIL`, and `CONTACT_EMAIL`, and records delivery status/error fields on the saved message.

## Draft Behavior

All content supports `is_draft`.

- Draft items are excluded from public-facing views, search results, feeds, and tag usage counts. Public querysets should always use `is_draft=False` (for example: `Entry.objects.filter(is_draft=False, ...)`).
- Draft records remain visible only in admin workflows.

## Search and Feeds

- Search is in `blog/search.py`; each model exposes `index_components()` with weighted fields.
- Search route: `/search/?q=<query>`.
- Feeds in `blog/feeds.py`:
  - `/atom/entries/`
  - `/atom/links/`
  - `/atom/everything/`
  - `/sitemap.xml`
- Feed endpoints are wrapped by `feedstats.utils.count_subscribers(...)`.

## Static, Media, and Images

- `STATIC_ROOT` → `staticfiles/`, `STATIC_URL` = `/static/`
- `MEDIA_ROOT` is project root, `MEDIA_URL` = `/`
- Static served with WhiteNoise (compressed).
- Photos are generated via `django-pictures` with responsive outputs (including AVIF) and multiple ratios/densities.

## Middleware/Helpers to Know

- `django_htmx.middleware.HtmxMiddleware` adds `request.htmx`; use it for HTMX fragment responses instead of manual HTMX header parsing.
- `blog.middleware.AmpersandRedirectMiddleware`
- `blog.context_processors.all`
- Custom tag renaming: `Tag.rename_tag(new_name)` creates `PreviousTagName` records/redirect support.

## Key Developer Commands

Use `uv` for Python/Django commands, and `just` for common project shortcuts.

- `just` / `just default` — run development server.
- `uv run manage.py runserver 0.0.0.0:8003` — explicit runserver.
- `uv run pytest` (or `just test`) — run tests.
- `uv run pytest -k <name>` / `uv run pytest -m "not slow"` / `uv run pytest blog/tests.py`.
- `uv run manage.py makemigrations` and `uv run manage.py migrate` — DB migrations.
- `just static` / `uv run manage.py collectstatic` — static build.
- `uv run manage.py import_blog_json <URL-or-path> --tag_with <tag>` or `uv run manage.py import_blog_xml --xmldir <path>` for imports.
