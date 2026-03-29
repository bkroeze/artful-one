---
id: dr7-qlcx
status: open
deps: []
links: []
created: 2026-03-29T01:05:28Z
type: task
priority: 2
assignee: Bruce Kroeze
---
# Verify search_document field implementation

blog/admin.py:30 excludes search_document field and uses it for PostgreSQL full-text search (lines 39-41). However, the field is not defined in models.py - it only exists in migrations. This PostgreSQL-specific feature may cause issues with SQLite. Verify the field is properly defined and consider making search work cross-database or documenting PostgreSQL requirement.

