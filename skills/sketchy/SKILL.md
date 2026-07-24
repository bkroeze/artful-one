---
name: sketchy
description: Use when creating, inspecting, updating, or deleting private working sketches, or when uploading and managing their temporary media through Sketchy.
---

# Sketchy

Use Sketchy for private, owner-scoped working sketches and their temporary media. It is appropriate when the task involves a D3, Processing.js, or raw JavaScript/HTML sketch; inspecting live sketch state; or providing uploaded assets to a sketch.

## Invocation and authentication

Run the repository-local executable from the repository root. Do not assume a global installation:

```sh
./bin/sketchy --help
```

Set `SKETCHY_TOKEN` to the **full raw token** returned when the token was issued:

```sh
export SKETCHY_TOKEN='<full-raw-token>'
```

The 16-character token prefix is only an identifier for administration and logs. It is not a bearer credential and must not be used as `SKETCHY_TOKEN`.

The default site is `https://artful.one`. Override it with `SKETCHY_URL` or with the global `--site` option. `--site` must precede the subcommand:

```sh
SKETCHY_URL=https://example.com ./bin/sketchy list
./bin/sketchy --site http://localhost:8000 list
```

Commands are non-interactive and return structured TOON, except `skill`, which returns raw Markdown.

## Sketch CRUD

List compact sketch summaries, or request the complete list schema:

```sh
./bin/sketchy list
./bin/sketchy list --full
```

Inspect one sketch. Use `--full` when untruncated JavaScript and HTML are required:

```sh
./bin/sketchy get <slug>
./bin/sketchy get <slug> --full
```

Create a sketch with `d3`, `processing`, or `raw` type:

```sh
./bin/sketchy create --slug <slug> --title "<title>" --type d3
```

For substantial JavaScript or HTML, write UTF-8 files and pass their paths instead of fighting shell quoting:

```sh
./bin/sketchy create --slug <slug> --title "<title>" --type raw \
  --startup-js-file ./sketch.js --div-html-file ./sketch.html
./bin/sketchy update <slug> \
  --startup-js-file ./sketch.js --div-html-file ./sketch.html
```

Update only supplied fields. Rename with `--new-slug`:

```sh
./bin/sketchy update <slug> --title "<new-title>"
./bin/sketchy update <slug> --new-slug <new-slug> --type d3
```

Deletes never prompt:

```sh
./bin/sketchy delete <slug>
```

Deleting an already-absent sketch is a successful no-op.

## Media

Upload a file, optionally associating it with a sketch or setting a lifetime:

```sh
./bin/sketchy media upload ./image.png --sketch <slug>
./bin/sketchy media upload ./preview.webp --expires-in-hours 24
```

Uploads return a stable `sketchy-media://<uuid>` reference. Put that reference in sketch JavaScript or HTML when the sketch needs the asset; do not substitute the temporary signed URL.

List compact media summaries or the complete API schema, and inspect by UUID or reference:

```sh
./bin/sketchy media list
./bin/sketchy media list --full
./bin/sketchy media get sketchy-media://<uuid>
```

Media deletes also never prompt, and deleting already-absent media is a successful no-op:

```sh
./bin/sketchy media delete sketchy-media://<uuid>
```
