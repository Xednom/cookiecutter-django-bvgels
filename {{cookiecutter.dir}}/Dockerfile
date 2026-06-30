# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.8

# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------
FROM base AS builder

ARG POETRY_VERSION
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# ---------------------------------------------------------------------------
# Production
# ---------------------------------------------------------------------------
FROM base AS production

RUN apt-get update && apt-get install --no-install-recommends -y \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the virtual environment created by Poetry
COPY --from=builder /app/.venv /app/.venv

# Make sure we use the venv binaries
ENV PATH="/app/.venv/bin:$PATH"

COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]

# ---------------------------------------------------------------------------
# Development override (docker-compose.yml sets this)
# ---------------------------------------------------------------------------
# You can override CMD in docker-compose.yml to run:
#   python manage.py runserver 0.0.0.0:8000
