FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

# Run as non-root user for security best practices
RUN adduser -D appuser
USER appuser

# Expose the port the app runs on (not required)
EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]