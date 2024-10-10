#!/bin/sh

if [ "$ENVIRONMENT" = "development" ]; then
    echo "Running in development mode"
    exec uv run python manage.py runserver 0.0.0.0:8000
else
    echo "Running in production mode"
    exec uv run gunicorn a_core.wsgi:application --bind 0.0.0.0:8000 --log-level=info
fi