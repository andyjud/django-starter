#!/bin/sh

alias uvm="uv run python manage.py"

# Run database migrations
uvm migrate

# Collect static files
uvm collectstatic --noinput

# Execute the CMD
exec "$@"