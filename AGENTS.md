
# AGENTS.md

This file provides guidance to AI Agents when working with code in this repository.

## Task tracking

- use the `beads-mcp` mcp server, or else the `bd` cli command to manage tasks.

## About This Project

This is a Django-based personal blog site for Artful.One, inspired by Simon Willison's blog architecture. The project supports multiple content types (entries, blogmarks, quotations, notes) with tagging, search, and RSS feeds.

## Development Environment Setup

This project uses Nix with flakes for environment management:

```bash
nix develop
```

This provides Python 3.13, uv (package manager), just (task runner), and all project dependencies.

## Common Commands

### Running the Development Server
```bash
just          # Default: runs development server
uv run manage.py runserver
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
  - Models: Entry, Blogmark, Quotation, Note, Tag, Series, Photo, PhotoTag, Photoset
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

### Django Hosts
The project uses `django-hosts` for subdomain routing:
- `www` - Main site (ROOT_URLCONF)
- `2003` - Legacy URLs (config.urls_2003)

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
- Searches across Entry, Blogmark, Quotation, and Note
- Uses `index_components()` method on each model (returns dict with A/B/C weighted fields)
- Search endpoint: `/search/?q=<query>`

## Testing

Tests use pytest with pytest-django and factory-boy:
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
- `CLOUDFLARE_EMAIL`, `CLOUDFLARE_TOKEN`, `CLOUDFLARE_ZONE_ID` - Cloudflare integration
- `SENTRY_DSN` - Sentry error tracking
- `SCREENSHOT_SECRET` - Secret for screenshot card generation
- `STAGING` - Staging environment flag
- `PICTURES_LOG_LEVEL`, `BLOG_LOG_LEVEL`, `DJANGO_LOG_LEVEL` - Logging levels

## Database

- Default: SQLite (`artful-one.db` in project root)
- Production: PostgreSQL via `DATABASE_URL` environment variable
- Migrations in `blog/migrations/`, `monthly/migrations/`, `feedstats/migrations/`
- Use `--reuse-db` flag with pytest to speed up test runs

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
