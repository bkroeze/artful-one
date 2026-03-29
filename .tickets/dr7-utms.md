---
id: dr7-utms
status: open
deps: []
links: []
created: 2026-03-29T01:04:45Z
type: bug
priority: 0
assignee: Bruce Kroeze
---
# Fix broken BeautifulSoup import in import_quora.py

The file blog/management/commands/import_quora.py uses the old BeautifulSoup 3.x import syntax: from BeautifulSoup import BeautifulSoup as Soup. This should be changed to: from bs4 import BeautifulSoup as Soup to match the beautifulsoup4==4.12.3 dependency in pyproject.toml. Currently this command will fail with ImportError.


## Notes

**2026-03-29T01:05:46Z**

IMPLEMENTATION NOTES:

**Location:** blog/management/commands/import_quora.py:8

**Current broken code:**


**Fix:**


**Why this matters:**
- BeautifulSoup 3.x used 'BeautifulSoup' as the package name
- BeautifulSoup 4.x uses 'bs4' as the package name
- Project has beautifulsoup4==4.12.3 in dependencies
- The current import will fail with ImportError when the command is run

**Testing:** After fix, verify with:


**Priority justification:** This is a broken import that makes an entire management command unusable.
