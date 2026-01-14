default: 
  uv run manage.py runserver 0.0.0.0:8003

static: 
  uv run manage.py collectstatic

test:
  uv run pytest
  
ruff:
  uv run ruff check

ruff-fix:
  uv run ruff check --fix

ruff-format:
  uv run ruff format

ruff-format-check:
  uv run ruff format --check

check:
  uv run manage.py check
  uv run ruff check

