#!/usr/bin/env bash
set -euo pipefail

# If running as root, make sure persistent directories are owned by appuser
#if [ "$(id -u)" = "0" ]; then
#  mkdir -p /storage/media /app/staticfiles
#  chown -R appuser:appuser /app /storage/media
#  exec gosu appuser "$0" "$@"
#fi

# We are running as appuser now
mkdir -p /storage/media /storage/sketchy-media /app/staticfiles

# Run database migrations
migration_version=2
migration_lock="/storage/MIGRATE.v${migration_version}.lock"
if [ ! -f "$migration_lock" ]
then
  echo "Running migration setup version ${migration_version}"
  ./.venv/bin/python manage.py migrate --noinput
  ./.venv/bin/python manage.py collectstatic --noinput
  touch "$migration_lock"
fi

: "${OPENROUTER_API_KEY:?OPENROUTER_API_KEY must be set}"

./.venv/bin/llm keys set openrouter --value "$OPENROUTER_API_KEY"

# Start Gunicorn
exec ./.venv/bin/gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT:-8001}" \
  --workers "${WEB_CONCURRENCY:-2}"
