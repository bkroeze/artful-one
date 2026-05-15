
# AGENTS.md

This file provides guidance to AI Agents when working with code in this repository.

## About This Project

This is a Django-based personal blog site for Artful.One, inspired by Simon Willison's blog architecture. The project supports multiple content types (entries, blogmarks, quotations, notes) with tagging, search, and RSS feeds.

## Core Commands

Most commands are either already in the Justfile, and managed by "just", or else are standard python/django,
accessed via `uv ...`

- start server: `uv run manage.py runserver 0.0.0.0:8003` - may change port to avoid contention
- create Django migration: `just makemigrations <django app, such as "blog">
- test: `uv run pytest`

### Best Practices

- Never directly run Python, always use `uv`

# Progress

Agent notes go here, regarding architectural patterns learned and explicit "remember this" requests during user interaction. Be extremely terse, optimized for AI token usage and ease of agent interpretation for future sessions.  Do not put "completed task x" here - put task notes in the task system.

### Running the Development Server
```bash
just          # Default: runs development server
```

### Testing
```bash
just test     # Run all tests
uv run pytest                    # Run all tests
uv run pytest blog/tests.py      # Run specific test file
uv run pytest -k test_homepage   # Run specific test by name
uv run pytest -m "not slow"      # Skip slow tests
```

### Database Migrations
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

### Static Files
```bash
just static   # Collect static files
uv run manage.py collectstatic
```

### Admin and Shell
```bash
uv run manage.py createsuperuser
uv run manage.py shell
```

### Import Commands
```bash
# Import blog content from JSON
uv run manage.py import_blog_json <URL-or-path> --tag_with <tag>

# Import from XML
uv run manage.py import_blog_xml --xmldir <path>
```

## Architecture Overview

### Project Structure
- `config/` - Django settings, URLs, and WSGI configuration
  - `settings.py` - Main settings with environment-based configuration
  - `urls.py` - URL routing (includes django-hosts for subdomain support)
  - `hosts.py` - Subdomain routing configuration
- `blog/` - Core blog application
  - All content types inherit from `BaseModel` (created, tags, slug, metadata, series, is_draft)
- `monthly/` - Monthly archives functionality
- `feedstats/` - Feed subscriber tracking
- Pixel border editor - Provided by the external `pixel-borders` dependency, with site-level template overrides under `templates/pixelborders/`
- `photos/` - Photo storage directory (contains AVIF/JPG files)
- `templates/` - Django templates
- `static/` - Static assets (CSS, JS)
- `staticfiles/` - Collected static files for production

### Content Types
All blog content inherits from `BaseModel` which provides:
- `created` - DateTimeField with timezone support
- `tags` - ManyToMany relationship with Tag
- `slug` - SlugField for URLs
- `metadata` - JSONField for extra data
- `import_ref` - Unique reference for imports
- `card_image` - Optional social card image
- `series` - Optional ForeignKey to Series
- `is_draft` - Boolean flag for draft status

**Entry**: Blog posts with title, body, optional custom template, and optional uploaded `Photo` displayed floated at the top with nullable `picture_size` width
**Blogmark**: Links with commentary (title, URL, commentary)
**Quotation**: Quotes with source and optional context
**Note**: Short-form content with optional title

Markdown entries render through the shared `markdownify` filters, including pipe table support on entry pages and list excerpts.

### URL Structure
Content URLs follow the pattern: `/{YYYY}/{Mon}/{D}/{slug}/`
- Example: `/2024/Oct/15/my-blog-post/`
- Short URLs available: `/e/{id}/`, `/b/{id}/`, `/q/{id}/`, `/n/{id}/`

## Configuration

Settings are in `config/settings.py` with environment variable support via `.env` file.

### Key Settings
- Uses SQLite by default (`artful-one.db`)
- `DATABASE_URL` can point to PostgreSQL or a mounted SQLite path such as Fly's `/data/artful-one.db`
- Static files served by WhiteNoise with compression
- Debug toolbar enabled in DEBUG mode
- django-pictures for responsive images

### Context Processor
`blog.context_processors.all` adds blog-specific context to all templates.

## Search Implementation

Search is implemented in `blog/search.py`:
- Uses `index_components()` method on each model (returns dict with A/B/C weighted fields)
- Search endpoint: `/search/?q=<query>`

## Testing

Tests use pytest with pytest-django:
- `conftest.py` configures Django for pytest
- `pytest.ini` sets DJANGO_SETTINGS_MODULE and test discovery patterns
- Factories defined in `blog/factories.py` for test data generation
- Test files: `blog/tests.py`, `monthly/tests.py`, `feedstats/tests.py`

Test markers:
- `@pytest.mark.slow` - Slow tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.django_db(transaction=True)` - Database tests

## Static Files and Media

- `STATIC_ROOT`: defaults to `staticfiles/`; Fly uses `/data/staticfiles`
- `STATIC_URL`: `/static/`
- `MEDIA_ROOT`: defaults to project base directory; Fly uses `/data`
- `MEDIA_URL`: `/`
- Uses WhiteNoise for static file serving with compression

Photos are stored in the `photos/` directory with django-pictures handling responsive image generation (AVIF format, multiple breakpoints and pixel densities). Entries can reference uploaded photos and use `picture_size` as the rendered container width.

## Feeds and Syndication

RSS/Atom feeds defined in `blog/feeds.py`:
- `/atom/entries/` - Blog entries only
- `/atom/links/` - Blogmarks only
- `/atom/everything/` - All content types
- `/sitemap.xml` - XML sitemap

Feed views wrapped with `count_subscribers()` from `feedstats.utils` for analytics.

## Draft Content

All content types support draft mode via `is_draft` boolean field:
- Draft items excluded from public views, search, feeds, and tag counts
- Draft items accessible via admin interface
- Use `is_draft=False` in querysets for public content

## Important Patterns

### Custom Template for Entries
Entries can specify `custom_template` field to use alternative templates.

### Tag Renaming
Tags support renaming via `tag.rename_tag(new_name)` which creates a `PreviousTagName` record and handles redirects.

### Photo Management
Photos use `PictureField` from django-pictures with:
- Automatic responsive image generation
- Multiple aspect ratios: [None, "1/1", "3/2", "16/9"]
- AVIF format output
- Pixel densities: [1, 2]
- Optional entry-level photo rendering via `Entry.photo` and `Entry.picture_size`

### Sketch Loading
Sketches are JS/P5 artifacts loaded by naming convention:
- Source sketches live in `sketches/art/<slug>.ts`; shared TS helpers live under `sketches/art/lib/`
- `uv run manage.py compile_sketches` bundles each non-lib `.ts` file to `static/art/<slug>.js`
- `Sketch.slug` must match the compiled JS basename
- `sketch_detail` passes `script_url = "art/{sketch.slug}.js"` and renders `<div id="{{ sketch.slug }}" data-height="600" data-width="800"></div>`
- Each sketch module should use the same slug as its DOM id, e.g. `const NAME = "lotus"; new p5(sketch, document.getElementById(NAME))`
- The detail template loads `/static/js/p5/p5.min.js` first, then the compiled `/static/art/<slug>.js`

### Middleware
- `django_htmx.middleware.HtmxMiddleware` - Adds `request.htmx` for HTMX fragment responses
- `blog.middleware.AmpersandRedirectMiddleware` - Custom URL handling
- WhiteNoise for static files
- django-hosts for subdomain routing

## Environment Variables

Key environment variables (loaded via python-dotenv):
- `DJANGO_SECRET` - Secret key (uses dev default if not set)
- `DJANGO_DEBUG` - Enable debug mode
- `DATABASE_URL` - Database URL; defaults to SQLite in project root and may point to PostgreSQL or a mounted SQLite path
- `ALLOWED_HOSTS` - Comma-separated host allowlist
- `CSRF_TRUSTED_ORIGINS` - Comma-separated list
- `STATIC_ROOT` - Static collection directory (defaults to `staticfiles/`)
- `MEDIA_ROOT` - Media file root (defaults to project root)
- `FILEDROP_BASE_DIR` - Filedrop storage directory (defaults to `filedrop_files/`)
- `SESSION_COOKIE_DOMAIN` - Cookie domain
- `SESSION_COOKIE_SECURE` - Require secure session cookies in production
- `PORT` - Bind port for the Fly/runtime entrypoint (defaults to 8000)
- `WEB_CONCURRENCY` - Gunicorn worker count for Fly/runtime entrypoint (defaults to 3)
- `STAGING` - Staging environment flag
- `MAILGUN_API_KEY`, `MAILGUN_DOMAIN`, `MAILGUN_API_URL`, `MAILGUN_FROM_EMAIL` - Contact form Mailgun delivery
- `CONTACT_EMAIL` - Contact form recipient email
- `PICTURES_LOG_LEVEL`, `BLOG_LOG_LEVEL`, `DJANGO_LOG_LEVEL` - Logging levels

## Database

- Default: SQLite (`artful-one.db` in project root)
- Migrations in `blog/migrations/`, `monthly/migrations/`, `feedstats/migrations/`
- Use `--reuse-db` flag with pytest to speed up test runs
