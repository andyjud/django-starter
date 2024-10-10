FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

# Expose the port the app runs on (not required)
EXPOSE 8000