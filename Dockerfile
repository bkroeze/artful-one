# syntax=docker/dockerfile:1

# Use Python 3.13 slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STATIC_ROOT=/app/staticfiles
ENV MEDIA_ROOT=/storage/media

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    wget \
    git \
    gosu \
    sqlite3 \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy project
COPY . .

# Run optional setup steps
RUN uv run llm install llm-openrouter || true

# Run collectstatic during build so the image is self-contained and startup is fast
RUN DJANGO_SECRET=build-time-dummy-secret \
    DATABASE_URL=sqlite:///:memory: \
    uv run manage.py collectstatic --noinput

# Create a non-root user
RUN chmod +x /app/bin/singleserver-entrypoint.sh \
    && useradd -m appuser \
    && mkdir -p /storage/media /storage/sketchy-media /app/sketchy-media \
    && chown -R appuser:appuser /app /storage

# Expose port
EXPOSE 8001

# Run migrations, then start gunicorn
CMD ["/app/bin/singleserver-entrypoint.sh"]
