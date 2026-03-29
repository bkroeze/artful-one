---
id: dr7-ninn
status: open
deps: []
links: []
created: 2026-03-29T01:04:56Z
type: cleanup
priority: 1
assignee: Bruce Kroeze
---
# Fix commented URL patterns in urls.py

Lines 161 and 165 in config/urls.py contain commented-out URL patterns. Line 161: # (r'^about/$', blog_views.about) - redundant since /about/ is already defined at line 140. Line 165: # re_path(r'^static/', static_redirect) - references undefined static_redirect function which would crash if uncommented. Remove both commented lines.


## Notes

**2026-03-29T01:06:10Z**

IMPLEMENTATION NOTES:

**Location:** config/urls.py lines 161 and 165

**Line 161:**

- This is redundant because /about/ is already defined at line 140
- The regex syntax is old (url() instead of re_path())
- Remove this line

**Line 165:**

- References undefined 'static_redirect' function
- Would cause NameError if uncommented
- No evidence this feature was ever implemented
- Remove this line

**Files affected:**
- config/urls.py (remove 2 lines)

**Testing:**
- Verify /about/ still works (line 140 should remain)
- Verify no errors on server startup
