---
id: dr7-gvuv
status: open
deps: []
links: []
created: 2026-03-29T01:04:48Z
type: cleanup
priority: 0
assignee: Bruce Kroeze
---
# Remove dead screenshot card code

The screenshot_card view in blog/views.py immediately raises Http404('Card not enabled') at line 901. All code after this line (lines 901-973, approximately 70 lines including helper functions generate_screenshot_url and _make_message) is unreachable dead code. Also remove the SCREENSHOT_EXTRA_CSS constant (lines 868-897) which is unused. The URL pattern /card/(.*)$ in config/urls.py:111 should also be removed or the feature fully implemented.

