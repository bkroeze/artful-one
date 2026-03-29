---
id: dr7-14om
status: open
deps: []
links: []
created: 2026-03-29T01:05:03Z
type: bug
priority: 2
assignee: Bruce Kroeze
---
# Fix missing urls_2003.py for subdomain routing

config/hosts.py:7 references config.urls_2003 for the 2003 subdomain, but this file does not exist. Either create the missing urls_2003.py file or remove the host pattern from hosts.py if the subdomain is no longer needed.

