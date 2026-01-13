---
id: aod-cb5b
status: closed
deps: []
links: []
created: 2026-01-13T19:34:50Z
type: task
priority: 1
assignee: droid
---
# Integrate `ruff` checker/formatter

Install `ruff` using `uv`, and integrate with Justfile so that `just check` does the django check and also does a ruff check. Add another "fix the files" command with ruff


## Notes

**2026-01-13T19:37:40Z**

Added ruff as a dev dependency via uv; updated Justfile so System check identified no issues (2 silenced).
All checks passed! runs Django system check + , and added All checks passed!, All checks passed!, 60 files left unchanged, 60 files already formatted. Ran System check identified no issues (2 silenced).
All checks passed! + ============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.6.0
django: settings: config.settings (from option)
rootdir: /home/bruce/work/artful-one-django
configfile: pytest.ini
plugins: django-4.2.0, django-test-plus-2.2.4, anyio-4.12.0, Faker-39.0.0
collected 32 items

feedstats/tests.py .                                                     [  3%]
monthly/tests.py ...                                                     [ 12%]
blog/tests.py ............................                               [100%]

=============================== warnings summary ===============================
feedstats/tests.py::TestFeedstats::test_feedstats_records_subscriber_numbers
  /home/bruce/work/artful-one-django/.venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py:1023: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    return self._get_default()

feedstats/tests.py::TestFeedstats::test_feedstats_records_subscriber_numbers
  /home/bruce/work/artful-one-django/.venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py:1670: RuntimeWarning: DateTimeField Photoset.created received a naive datetime (2026-01-13 19:37:36.447976) while time zone support is active.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 32 passed, 2 warnings in 3.52s ======================== successfully; applied .
