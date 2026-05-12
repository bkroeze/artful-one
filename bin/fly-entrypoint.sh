#!/usr/bin/env bash
set -euo pipefail

mkdir -p /data/staticfiles /data/filedrop_files /data/backups

uv run manage.py migrate --noinput
uv run manage.py collectstatic --noinput

exec uv run gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --workers "${WEB_CONCURRENCY:-3}"
