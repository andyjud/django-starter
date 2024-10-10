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

# Set the entrypoint to the entrypoint.sh file
ENTRYPOINT ["./entrypoint.sh"]

# Set a default command that can be overridden at runtime
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]