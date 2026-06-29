set dotenv-load := true

IMAGE_REGISTRY := "ghcr.io"
IMAGE_OWNER := "bkroeze"
IMAGE_NAME := "artful-one"
IMAGE_TAG := "latest"
IMAGE := IMAGE_REGISTRY + "/" + IMAGE_OWNER + "/" + IMAGE_NAME + ":" + IMAGE_TAG

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

# Build Docker image locally
docker-build:
    docker build -t {{IMAGE}} .

# Run tests and checks inside the Docker container to verify the build
docker-test:
    docker run --rm -e DJANGO_SECRET=test-secret-key-for-checks-and-verification -e DATABASE_URL=sqlite:///:memory: {{IMAGE}} uv run manage.py check
    docker run --rm -e DJANGO_SECRET=test-secret-key-for-checks-and-verification -e DATABASE_URL=sqlite:///:memory: {{IMAGE}} uv run pytest

# Push the Docker image to GHCR (requires `docker login ghcr.io`)
docker-push:
    docker push {{IMAGE}}

