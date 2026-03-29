---
id: dr7-3mcu
status: open
deps: []
links: []
created: 2026-03-29T01:05:08Z
type: task
priority: 2
assignee: Bruce Kroeze
---
# Update Sentry integration to modern SDK

Settings.py:99-106 uses raven (legacy Sentry SDK) with INSTALLED_APPS += ('raven.contrib.django.raven_compat',). Raven is deprecated. Update to use modern sentry-sdk instead. See https://docs.sentry.io/platforms/python/integrations/django/

