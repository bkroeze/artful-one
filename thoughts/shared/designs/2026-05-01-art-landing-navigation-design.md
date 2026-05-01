# 2026-05-01 Art Landing Navigation Design

## Problem Statement
The current experience presents two top-level art entry points in the primary navigation, with both **Art** and **Sketches** visible as separate links. These currently lead to distinct discovery pages:

- **Art** currently opens a photo-collection-by-tag browsing page.
- **Sketches** currently opens the sketch grid landing with links to individual sketch detail views.

This split causes duplicated entry into the same conceptual space. The intent is to make **one primary Art destination** and present both content streams in a single, coherent landing experience while keeping sketch detail access stable.

## Constraints
- Current behavior shows both "Art" and "Sketches" in the primary navigation across all menu variants.
- The `/art/` destination is the current photo-collection-by-tag browsing page.
- The `/sketch/` destination is the current sketch grid listing.
- Per-sketch detail pages are currently accessible from sketch list items.
- `/sketches/` is not currently routed; any alias or redirect should be treated as a separate compatibility decision.
- The design should remain implementation-agnostic and avoid exact implementation references.
- Existing routes that already receive traffic should stay stable unless a deliberate compatibility decision is made.

## Approach
1. Change primary navigation to a single **Art** link that points to `/art/`, and remove the separate **Sketches** top-level entry.
2. Redesign the `/art/` landing experience into one composed page with two clearly separated sections:
   - **Live Art Code**
   - **Galleries**
3. Keep `/sketch/` and sketch detail compatibility by default so existing external and internal links continue to work.
4. `/sketches/` is not currently routed; any alias or redirect should be treated as a separate compatibility decision.
5. Keep implementation scope focused: composition and labeling should reuse existing content patterns and behaviors conceptually rather than introducing duplicate visual paradigms.

## Architecture
The page becomes a single entry experience instead of two separate top-level surfaces.

- **Entry:** users reach the unified destination at `/art/`.
- **Content:** aggregate two content sets for display:
  - sketch items with metadata and links
  - photo collection cards/listing with preview imagery and counts, sourced from the existing photo collection cards/listing currently shown on `/art/`.
- **Presentation:** render both content sets in sequence under the existing global page shell with clear section boundaries.

This preserves the sketch item detail journeys while shifting first discovery of sketches to the unified landing.

## Components
- **Primary navigation**
  - Replace separate Art and Sketches links with a single Art link.
  - Apply this consistently in fixed, sidebar, and masthead variants.
- **`/art/` landing page layout**
  - Top section: **Live Art Code**
  - Second section: **Galleries**
- **Live Art Code section**
  - Reuses the current sketch list behavior and interaction model.
- **Galleries section**
  - Reuses the existing photo collection cards/listing behavior and interaction model from `/art/`.
- **Sketch deep links**
  - Keep existing sketch detail behavior intact for compatibility.

## Data Flow
- **When visiting `/art/`:**
  1. Load the current `/art/` list and reuse it as the source for the Galleries section.
  2. Fetch current sketch list data for the Live Art Code section.
  3. Render both sections in one page while preserving each section’s independent empty state handling.
- **For sketch compatibility:**
  1. Keep the current sketch listing at `/sketch/` available.
  2. Keep per-sketch detail links and pages in place through the existing sketch link flow.
- **For `/sketches/`:**
  - `/sketches/` is not currently routed; any alias or redirect should be treated as a separate compatibility decision.

## Error Handling
- Preserve existing empty-state messaging for both content streams (e.g., no sketches available / no galleries available).
- Preserve existing empty-state messaging patterns used on the current `/art/` landing output for the Galleries section.
- If one content stream is unavailable, the other stream should remain visible so the page stays usable.
- Keep sketch detail behavior unchanged so existing links and user flows continue to work.
- Ensure the redesigned primary nav always points to valid destinations.

## Testing Strategy
- Validate that only one primary nav item for art exists (Art only) across all menu variants and points to `/art/`.
- Validate user journeys:
  - `/art/` renders both **Live Art Code** and **Galleries**.
  - `/sketch/` continues to return sketch listing behavior.
  - sketch detail pages remain reachable through existing paths.
- `/sketches/` is not currently routed; any alias or redirect should be treated as a separate compatibility decision.
- Validate visible structure/content:
  - both section headers appear when data exists
  - section-level counts and links are coherent and functional.
- Regression check that gallery and sketch links still resolve to their intended existing pages.

## Open Questions
1. Should `/sketches/` stay unrouted, or should an alias/redirect be introduced as a compatibility decision?
2. Should the unified `/art/` landing present both sections on a single continuous page or within tabs/accordions?
3. Are there additional SEO/accessibility refinements needed for section hierarchy beyond current patterns?
4. Should shared side/secondary UI from both current experiences be merged or standardized into one pattern?
