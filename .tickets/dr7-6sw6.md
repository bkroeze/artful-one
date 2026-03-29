---
id: dr7-6sw6
status: open
deps: []
links: []
created: 2026-03-29T01:05:30Z
type: task
priority: 3
assignee: Bruce Kroeze
---
# Review custom_template field usage

blog/models.py:242 defines custom_template CharField for Entry model. Check if any entries actually use custom templates. If not used, consider removing this feature to simplify the codebase. It's referenced in views.py:91.

