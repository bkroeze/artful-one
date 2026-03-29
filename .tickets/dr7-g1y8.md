---
id: dr7-g1y8
status: open
deps: []
links: []
created: 2026-03-29T01:05:06Z
type: task
priority: 2
assignee: Bruce Kroeze
---
# Resolve django-sql-dashboard configuration

Settings.py:40 sets DASHBOARD_ROW_LIMIT = 200 for django-sql-dashboard, but the app is not in INSTALLED_APPS. Additionally, templates/django_sql_dashboard/base.html exists but is unused. Either: 1) Add django_sql_dashboard to INSTALLED_APPS and dependencies, or 2) Remove the setting and the unused template. Also remove the commented database configuration at lines 159-161 related to this.

