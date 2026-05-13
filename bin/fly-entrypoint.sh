#!/usr/bin/env bash
set -euo pipefail

if [ "$(id -u)" = "0" ]; then
  mkdir -p /data/staticfiles /data/filedrop_files /data/backups
  chown -R appuser:appuser /data
  exec gosu appuser "$0"
fi

mkdir -p /data/staticfiles /data/filedrop_files /data/backups

./.venv/bin/python manage.py migrate --noinput
./.venv/bin/python manage.py collectstatic --noinput

exec ./.venv/bin/gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --workers "${WEB_CONCURRENCY:-1}"
