---
id: aod-e725
status: closed
deps: []
links: [aod-f0d4]
created: 2026-01-15T15:22:17Z
type: feature
priority: 0
assignee: droid
---
# Add support for P5 typescript sketches

Add new Django app "sketches"

This app should have a Sketch model:
- name
- slug
- description
- image (uses the Photo model from `blog`)

The slug will directly correspond to a P5 Typescript file living at `/sketches/art/slug.ts`

Create a new command "compile-sketches", which compiles the sketches in /sketches/art/ to Javascript suitable for displaying the P5 sketch.

Create a landing page listing all the sketches, and linking out to a sketch detail page for each.

The sketch detail page should extend site_detail.html, showing the P5 sketch in the "primary" block, and have a "maximize" button to show full screen with no "wrapping" such as headers and footers.  It should also display the description for the art on the site detail page, but not when maximized.

Make initial sketch objects, no description needed for now, just with their names and slugs, so that we can see immediate results of this work.
