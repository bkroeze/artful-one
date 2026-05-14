# Personal blog site code for Artful.One

Based largely on [Simon Willison's Blog](https://github.com/simonw/simonwillisonblog)

## Development

This project uses [Nix](https://nixos.org/) to manage the development environment. To get started, make sure you have Nix installed with flakes enabled.

Then, to enter the development shell, run:

```bash
nix develop
```

This will provide you with a shell that has Python, Node.js, bun, and all the project dependencies available.

## Contact Form

The site contact form saves submissions and sends email through Mailgun when configured.

Set these environment variables for deployments that use the contact page:

- `MAILGUN_API_KEY`
- `MAILGUN_DOMAIN`
- `MAILGUN_API_URL` (defaults to `https://api.mailgun.net/v3`)
- `MAILGUN_FROM_EMAIL`
- `CONTACT_EMAIL`
