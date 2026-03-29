---
id: dr7-2g7t
status: open
deps: []
links: []
created: 2026-03-29T01:05:22Z
type: task
priority: 3
assignee: Bruce Kroeze
---
# Audit LiveUpdate model usage

blog/models.py:299-305 defines LiveUpdate model which appears to be for live blogging functionality. Check if this feature is still used. If not, consider removing the model and associated admin configuration (blog/admin.py:65-67).

