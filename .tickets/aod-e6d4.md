---
id: aod-e6d4
status: closed
deps: []
links: []
created: 2026-01-14T00:40:31Z
type: bug
priority: 2
assignee: 0xBigBee
---
# Fix the list of tables in /rpg/names/

Make sure to start with a confirming test, then fix it.

Currently, they render with a "null"

ex:
---
```
<div class="item selected" data-value="ad/ad1.1a" data-text="null&quot;
            &amp;gt;
              Adventure Design Locations (Overview)
            ">null"
            &gt;
              Adventure Design Locations (Overview)
            </div>
```