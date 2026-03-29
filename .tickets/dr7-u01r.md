---
id: dr7-u01r
status: open
deps: []
links: []
created: 2026-03-29T01:04:51Z
type: bug
priority: 0
assignee: Bruce Kroeze
---
# Remove broken comments_list template tags

In blog/templatetags/blog_tags.py, lines 31-50 define two template tags (comments_list and comments_list_with_headers) that reference a non-existent template includes/comments_list.html. Since the template is missing, these template tags are broken and will cause TemplateDoesNotExist errors if used. Either create the missing template or remove the broken template tags.


## Notes

**2026-03-29T01:06:01Z**

IMPLEMENTATION NOTES:

**Location:** blog/templatetags/blog_tags.py lines 31-50

**Broken code to remove:**


**Why:**
- Template includes/comments_list.html does not exist
- If these template tags are used, they will raise TemplateDoesNotExist
- No references to these tags found in templates/ directory
- Comment system may not be actively used

**Alternative (if comments ARE used):**
Create templates/includes/comments_list.html with appropriate comment rendering.

**Files to modify:**
- blog/templatetags/blog_tags.py (remove 20 lines)

**Testing:**
Search for any template usage: grep -r 'comments_list' templates/
