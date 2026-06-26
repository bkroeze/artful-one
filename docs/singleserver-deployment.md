# Single Server Deployment Runbook

The default `Dockerfile` is the Single Server image. It installs dependencies with `uv`, collects static files during the image build, and starts through `bin/singleserver-entrypoint.sh`.

## App Setup

Add or edit the app on the Single Server host with the repository URL, deployment branch, public domain, and healthcheck path:

```bash
ssh <host> 'singleserver add https://github.com/<owner>/<repo> \
  --name artful-one \
  --branch main \
  --domain artful.one \
  --healthcheck-path /health/ \
  --deploy-timeout 20m'
```

Use `singleserver edit artful-one ...` instead when the app already exists.

The healthcheck path is exact and must include the trailing slash. `/health/`
returns `text/plain` `ok\n` from the first Django middleware before normal host
routing, redirects, auth, or URL resolution.

## Persistent Storage and Env

Enable persistent storage at `/storage` before the first production deploy:

```bash
ssh <host> 'singleserver storage enable artful-one --mount /storage --no-deploy'
```

Set runtime configuration on the host, not in the repository:

```bash
ssh <host> 'singleserver env set artful-one DJANGO_SECRET=replace-me'
ssh <host> 'singleserver env set artful-one ALLOWED_HOSTS=artful.one'
ssh <host> 'singleserver env set artful-one CSRF_TRUSTED_ORIGINS=https://artful.one'
ssh <host> 'singleserver env set artful-one DATABASE_URL=sqlite:////storage/artful-one.db'
ssh <host> 'singleserver env set artful-one MEDIA_ROOT=/storage/media'
ssh <host> 'singleserver env set artful-one FILEDROP_BASE_DIR=/storage/filedrop_files'
```

Set Mailgun, Cloudflare, OpenRouter, Sentry, and other optional provider secrets only when those features are enabled. The image already sets `STATIC_ROOT=/app/staticfiles` and `MEDIA_ROOT=/storage/media`; the explicit `MEDIA_ROOT` env value keeps the deployment config visible on the host.

`singleserver env set` configures the runtime container, not the Docker build that runs `uv sync --frozen`. Do not set `GITHUB_DEPLOY_TOKEN` for this image. Git dependencies in `pyproject.toml` must be fetchable by the build without extra credentials, or they should be published to a package index or vendored into the app repository.

## Data Cutover

Freeze writes on the current deployment before copying data. Admin edits, imports, contact submissions, filedrop changes, and photo changes should wait until Single Server is live.

Create a SQLite backup from the current deployment source, then copy it into the mounted storage path used by `DATABASE_URL`:

```bash
sqlite3 artful-one.db ".backup 'artful-one-pre-singleserver.db'"
scp artful-one-pre-singleserver.db <host>:/srv/storage/artful-one/artful-one.db
```

Copy existing uploaded media into `/storage/media` during cutover. Photo migration `0014_alter_photo_image` only updates the field type; it does not copy older `Photo.image` files from static output or the repository.

## Deploy and Verify

Deploy the configured branch and inspect health:

```bash
ssh <host> 'singleserver deploy artful-one'
ssh <host> 'singleserver status'
ssh <host> 'singleserver doctor artful-one'
```

Verify the homepage, `/health/`, admin login, search, feeds, photo pages, filedrop, and contact form on the public domain.
