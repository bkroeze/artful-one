
# AGENTS.md

This file provides guidance to AI Agents when working with code in this repository.

## About This Project

This is a Django-based personal blog site for Artful.One, inspired by Simon Willison's blog architecture. The project supports multiple content types (entries, blogmarks, quotations, notes) with tagging, search, and RSS feeds.

## Task tracking

This project uses a CLI ticket system for task management. Run `tk help` when you need to use it.

## Core Commands

Most commands are either already in the Justfile, and managed by "just", or else are standard python/django,
accessed via `uv ...`

- start server: `uv run manage.py runserver 0.0.0.0:8003` - may change port to avoid contention
- create Django migration: `just makemigrations <django app, such as "blog">
- test: `uv run pytest`

## Integrating with Ticketing system (dependency-aware task planning)

Typical flow (agents)
1) **Pick ready work**
   - `tk ready` → choose one item (highest priority, no blockers)
2) **Work and update**
   - `tk add-note jd-123 "progress notes, including sub-tickets opened"`
3) **Complete and release**
   - Add notes to AGENTS.md in the "Progress" section.
   - `tk close jd-123`

### Best Practices

- Never directly run Python, always use `uv`
- Check `tk ready` at session start to find available work
- Update status as you work (in_progress → closed)
- Create new issues with `tk create` when you discover tasks
- Use descriptive titles and set appropriate priority/type

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

**Entry**: Blog posts with title, body, optional custom template
**Blogmark**: Links with commentary (title, URL, commentary)
**Quotation**: Quotes with source and optional context
**Note**: Short-form content with optional title

### URL Structure
Content URLs follow the pattern: `/{YYYY}/{Mon}/{D}/{slug}/`
- Example: `/2024/Oct/15/my-blog-post/`
- Short URLs available: `/e/{id}/`, `/b/{id}/`, `/q/{id}/`, `/n/{id}/`

## Configuration

Settings are in `config/settings.py` with environment variable support via `.env` file.

### Key Settings
- Uses SQLite by default (`artful-one.db`)
- Supports PostgreSQL via `DATABASE_URL` environment variable
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

- `STATIC_ROOT`: `staticfiles/` directory
- `STATIC_URL`: `/static/`
- `MEDIA_ROOT`: Project base directory
- `MEDIA_URL`: `/`
- Uses WhiteNoise for static file serving with compression

Photos are stored in the `photos/` directory with django-pictures handling responsive image generation (AVIF format, multiple breakpoints and pixel densities).

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

### Middleware
- `blog.middleware.AmpersandRedirectMiddleware` - Custom URL handling
- WhiteNoise for static files
- django-hosts for subdomain routing

## Environment Variables

Key environment variables (loaded via python-dotenv):
- `DJANGO_SECRET` - Secret key (uses dev default if not set)
- `DJANGO_DEBUG` - Enable debug mode
- `DATABASE_URL` - PostgreSQL connection string (optional)
- `CSRF_TRUSTED_ORIGINS` - Comma-separated list
- `SESSION_COOKIE_DOMAIN` - Cookie domain
- `STAGING` - Staging environment flag
- `PICTURES_LOG_LEVEL`, `BLOG_LOG_LEVEL`, `DJANGO_LOG_LEVEL` - Logging levels

## Database

- Default: SQLite (`artful-one.db` in project root)
- Migrations in `blog/migrations/`, `monthly/migrations/`, `feedstats/migrations/`
- Use `--reuse-db` flag with pytest to speed up test runs
