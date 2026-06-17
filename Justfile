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

fly-backup-db:
    backup="bak/artful-one-$(date +%y%m%d).db"; mkdir -p bak; test ! -e "$backup" || { echo "$backup already exists; refusing to overwrite"; exit 1; }; flyctl sftp get --app artful-one /data/artful-one.db "$backup"

fly-deploy-db:
    test -f artful-one.db
    flyctl ssh console --app artful-one --command 'set -eu; backup="/data/artful-one-$(date +%y%m%d).db"; if [ -e "$backup" ]; then echo "$backup already exists; refusing to overwrite"; exit 1; fi; mv /data/artful-one.db "$backup"'
    flyctl sftp put --app artful-one artful-one.db /data/artful-one.db

fly-logs:
    fly logs --app artful-one
