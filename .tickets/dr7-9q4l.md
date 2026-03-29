---
id: dr7-9q4l
status: open
deps: []
links: []
created: 2026-03-29T01:05:20Z
type: cleanup
priority: 3
assignee: Bruce Kroeze
---
# Review ancient URL redirects for removal

config/urls.py:125-128 has redirects for ancient URL patterns like //archive/2002/10/24/. The comment says these are still getting hits, but they may be from very old external links. Review analytics to see if these redirects are still needed after 20+ years, or if they can be removed to simplify URL routing.

