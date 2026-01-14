---
id: aod-77fa
status: closed
deps: []
links: []
created: 2026-01-13T21:30:49Z
type: epic
priority: 0
assignee: droid
---
# Create rpg Django app

Using the typescript code found in `/src`, convert to a Django new django app, to be a sibling of `blog`

You will need to analyse the existing code and make a Djano model for it.

The existing raw tables found in names.ts and adventure-design.ts should be converted into json files, with the migration script for it loading all files in the json import directory.  The load-from-json functionality should separately be captured as a `django manage` command, allowing for future tables to be easily entered.

Include django admin for these models, allowing the tables to be edited from the UI.

The "table-roller" functionality should be converted to Python to be used in when generating names using a form, and should include all options currently available in the bun command.

## The app page

The app itself should be done in "htmx" fashion.  Make a new htmx based root page and wire it up to work via htmx.  Then make a new app page, "rpg-names.html" which should be able to:
- Generate requested # of names
- Use the selected table or tables
- provide the appropriate options when using a table
- Show the resulting names
- Allow for names to be selected in the resulting name table, and then saved as favorites.
- Save favorite in a cookie and show at the bottom - the favorites should save the name and table selection leading to that name.

Use Fomantic UI for styling - you can look at the existing templates for this styling.
