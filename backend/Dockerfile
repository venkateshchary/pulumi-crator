FROM python:3.13-slim as builder

RUN mkdir -p /backend

WORKDIR /backend

# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# set environment variables
ENV UV_PYTHON=3.13

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/app/.venv

# install uv
COPY --from=ghcr.io/astral-sh/uv:0.8.14 /uv /uvx /bin/

# Since there's no point in shipping lock files, we move them
# into a directory that is NOT copied into the runtime image.
# The trailing slash makes COPY create `/_lock/` automagically.
COPY pyproject.toml .

RUN uv lock
# Synchronize dependencies.
# This layer is cached until uv.lock or pyproject.toml change.
# Install dependencies using uv's project management
RUN uv sync --frozen --no-dev

# copy project
COPY . /backend/

EXPOSE 8000

# Command for production
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]