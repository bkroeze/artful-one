set dotenv-load := true

default:
  uv run manage.py runserver 0.0.0.0:8003

static:
  uv run manage.py collectstatic --noinput

test:
  uv run pytest

ruff:
  uv run ruff check

ruff-fix:
  uv run ruff check --fix

ruff-format:
  uv run ruff format

ruff-format-check:
  uv run ruff format --check

check:
  uv run manage.py check
  uv run ruff check

compile-sketches:
  uv run manage.py compile_sketches

compile-sketches-clear:
  uv run manage.py compile_sketches --clear

icons *args:
  uv run python -m rpg_chargen.icons.cli {{args}}

fly-deploy:
    : "${GITHUB_DEPLOY_TOKEN:?Set GITHUB_DEPLOY_TOKEN in .env before deploying}"
    flyctl deploy --app artful-one --remote-only --build-secret GITHUB_DEPLOY_TOKEN="${GITHUB_DEPLOY_TOKEN}"

fly-logs:
    fly logs --app artful-one
