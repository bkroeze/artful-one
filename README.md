# Personal blog site code for Artful.One

Based largely on [Simon Willison's Blog](https://github.com/simonw/simonwillisonblog)

## Development

This project uses [Nix](https://nixos.org/) to manage the development environment. To get started, make sure you have Nix installed with flakes enabled.

Then, to enter the development shell, run:

```bash
nix develop
```

This will provide you with a shell that has Python, Node.js, bun, and all the project dependencies available.

## Deployment

The default `Dockerfile` targets Single Server. It runs `bin/singleserver-entrypoint.sh`, expects persistent uploaded media at `/storage/media`, and serves Gunicorn on `PORT` (default `8000`). See `docs/singleserver-deployment.md`.

Fly.io deployments use `fly.toml`, which selects `Dockerfile.flyio` and stores SQLite, static output, media, filedrop files, and backups on the `/data` volume. See `docs/flyio-deployment.md`.

For the one-time production database transition from SQLite to PostgreSQL, see `docs/postgresql-production-transition.md`.

Both deployment targets use the exact `/health/` path for health checks. The first Django middleware returns `text/plain` `ok\n` before normal host routing, redirects, auth, or URL resolution.

## Contact Form

The site contact form saves submissions and sends email through Mailgun when configured.

Set these environment variables for deployments that use the contact page:

- `MAILGUN_API_KEY`
- `MAILGUN_DOMAIN`
- `MAILGUN_API_URL` (defaults to `https://api.mailgun.net/v3`)
- `MAILGUN_FROM_EMAIL`
- `CONTACT_EMAIL`
