# Use Python 3.13 slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
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

RUN uv run llm install llm-openrouter

# Create a non-root user
RUN chmod +x /app/bin/fly-entrypoint.sh \
    && useradd -m appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data

# Expose port
EXPOSE 8000

# Run migrations, collect static files onto the mounted volume, then start gunicorn.
CMD ["/app/bin/fly-entrypoint.sh"]
