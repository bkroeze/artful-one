#!/usr/bin/env bash
set -euo pipefail

# If running as root, make sure persistent directories are owned by appuser
if [ "$(id -u)" = "0" ]; then
  mkdir -p /storage/media /app/staticfiles
  chown -R appuser:appuser /app /storage/media
  exec gosu appuser "$0" "$@"
fi

# We are running as appuser now
mkdir -p /storage/media /app/staticfiles

# Run database migrations
./.venv/bin/python manage.py migrate --noinput

# Start Gunicorn
exec ./.venv/bin/gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --workers "${WEB_CONCURRENCY:-2}"
