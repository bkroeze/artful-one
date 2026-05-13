# CODE_STYLE.md

Concise conventions for working in this Django repository.

## Command rules (required)
- **Do** use project wrappers:
  - `uv run pytest` (or file/marker variants) for tests
  - `just` for common project tasks
  - `uv run manage.py ...` for Django management commands
- **Don't** run `python` or `manage.py` directly.
- Prefer `uv run pytest -k ...` for targeted test runs while iterating.

## App boundaries
- **Do** keep features in their owning app:
  - `blog/` for content, tags, search indexing glue, RSS feeds
  - `monthly/` for archive behavior
  - `feedstats/` for feed subscriber tracking
  - `pixelborders/` for pixel border designs, editor fragments, generated CSS, and AI frame generation
  - `config/` for settings/URL/WSGI
- **Don't** cross-modify unrelated apps for logic that belongs to another domain.

## BaseModel/content model patterns
- **Do** follow existing BaseModel field patterns for new content models:
  - timezone-aware `created`, `slug`, `tags`, `metadata`, `import_ref`,
    `card_image`, `series`, `is_draft`
- **Do** model content behavior by type:
  - Entry, Blogmark, Quotation, Note inherit and extend BaseModel expectations.
- **Don't** introduce new public fields that duplicate existing content abstractions.

## Draft filtering (critical)
- **Do** enforce public visibility with `is_draft=False` in public querysets.
- **Do** apply this in:
  - public list/detail views
  - search results
  - feeds
  - tag/count aggregations
- **Don't** leak draft content outside admin/import paths.

## Search / feeds / static / media conventions
- **Do** keep search aligned with `blog/search.py` (`index_components`) and `search/?q=<query>`.
- **Do** keep feed routes consistent:
  - `/atom/entries/`, `/atom/links/`, `/atom/everything/`, `/sitemap.xml`
- **Do** leave `feedstats.utils.count_subscribers` wrapping feed views.
- **Do** respect static/media settings:
  - static: `STATIC_URL=/static/`, `STATIC_ROOT` defaults to `staticfiles/` and may be overridden by environment
  - media: `MEDIA_ROOT` defaults to project base and may be overridden by environment, `MEDIA_URL=/`
- **Don't** invent alternate feed/search URLs for existing routes.

## Testing style
- **Do** keep tests small and behavior-focused.
- **Do** use existing test locations (`blog/tests.py`, app-level tests) and markers:
  - `@pytest.mark.slow`, `@pytest.mark.integration`, `@pytest.mark.django_db(transaction=True)`
- **Don't** write broad integration tests when unit-level assertions are sufficient.

## Workflow / process
- **Do** add notes in `AGENTS.md > Progress` only for cross-session architectural reminders.
- **Don't** bypass existing conventions for command flow, model patterns, or routing.
