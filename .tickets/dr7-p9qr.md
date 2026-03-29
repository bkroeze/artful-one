---
id: dr7-p9qr
status: open
deps: []
links: []
created: 2026-03-29T01:05:13Z
type: bug
priority: 2
assignee: Bruce Kroeze
---
# Fix Photoset URL routing

blog/models.py:496-497 defines get_absolute_url() returning /photosets/{self.slug}/ but no URL pattern exists for this route. Either add the URL pattern or remove/modify the method to return a working URL. The photoset feature is used in archive_day view and admin.

