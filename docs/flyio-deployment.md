# Fly.io Deployment Runbook

This app runs on Fly.io as `artful-one`, with Cloudflare proxying `artful.one`.
The production machine is intentionally single-instance because it uses SQLite on
a Fly volume.

## Initial Setup

Create the app and volume:

```bash
fly apps create artful-one
fly volumes create artful_one_data --app artful-one --region lax --size 3 --snapshot-retention 30
```

Set required secrets:

```bash
fly secrets set --app artful-one \
  DJANGO_SECRET='replace-me' \
  MAILGUN_API_KEY='replace-me' \
  MAILGUN_DOMAIN='replace-me' \
  MAILGUN_FROM_EMAIL='replace-me' \
  CONTACT_EMAIL='replace-me'
```

Set optional secrets only if those production features are needed:

```bash
fly secrets set --app artful-one \
  CLOUDFLARE_EMAIL='replace-me' \
  CLOUDFLARE_TOKEN='replace-me' \
  CLOUDFLARE_ZONE_ID='replace-me' \
  OPENROUTER_API_KEY='replace-me' \
  SCREENSHOT_SECRET='replace-me' \
  SENTRY_DSN='replace-me'
```

Deploy the app once so Fly creates the machine:

```bash
fly deploy --app artful-one --remote-only
```

## Data Cutover

Freeze writes on the current deployment before copying the database. Admin edits,
imports, contact submissions, filedrop changes, and photo changes should wait
until Fly is live.

Create a local SQLite backup from the current deployment source:

```bash
sqlite3 artful-one.db ".backup 'artful-one-pre-fly.db'"
```

Upload the migrated database to the Fly volume:

```bash
fly ssh console --app artful-one -C "mkdir -p /data"
fly ssh sftp put --app artful-one artful-one-pre-fly.db /data/artful-one.db
```

Restart the app. The entrypoint creates volume directories, runs migrations, and
collects static files into `/data/staticfiles`.

```bash
fly machine restart --app artful-one
```

Verify before DNS cutover:

```bash
fly status --app artful-one
fly logs --app artful-one
curl -fsS https://artful-one.fly.dev/health/
```

Also check the homepage, admin login, search, feeds, photo pages, filedrop, and
contact form.

## Cloudflare Cutover

Keep Cloudflare proxy enabled for DDoS/WAF/cache protection.

Add the Fly certificate:

```bash
fly certs add artful.one --app artful-one
fly certs show artful.one --app artful-one
```

Update the Cloudflare DNS record for `artful.one` according to
`fly certs show`. After it is healthy, verify:

```bash
curl -fsS https://artful.one/health/
```

Once production traffic is confirmed on Fly, disable the old Cloudflare tunnel
route for this app.

## Daily Backup Cron

Run this from the home server. It creates a consistent SQLite backup on the Fly
volume, pulls it locally, and retains 30 daily backups.

```bash
#!/usr/bin/env bash
set -euo pipefail

APP="artful-one"
REMOTE_DIR="/data/backups"
LOCAL_DIR="/srv/backups/artful-one"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
NAME="artful-one-${STAMP}.db"

mkdir -p "${LOCAL_DIR}"

fly ssh console --app "${APP}" -C \
  "mkdir -p ${REMOTE_DIR} && sqlite3 /data/artful-one.db \".backup '${REMOTE_DIR}/${NAME}'\""

fly ssh sftp get --app "${APP}" "${REMOTE_DIR}/${NAME}" "${LOCAL_DIR}/${NAME}"

find "${LOCAL_DIR}" -name 'artful-one-*.db' -type f -mtime +30 -delete
```

Cron example:

```cron
15 3 * * * /usr/local/bin/backup-artful-one-fly
```

Periodically test restore by copying a backup to a temporary SQLite file and
running:

```bash
sqlite3 /path/to/backup.db "pragma integrity_check;"
```

## Restore

Freeze writes, upload the chosen backup as `/data/artful-one.db`, restart the
machine, and run the same smoke checks from the cutover section.

```bash
fly ssh sftp put --app artful-one \
  /srv/backups/artful-one/artful-one-YYYYMMDDTHHMMSSZ.db \
  /data/artful-one.db
fly machine restart --app artful-one
curl -fsS https://artful.one/health/
```
