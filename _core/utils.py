import os

from django.core.management.utils import get_random_secret_key


def get_secret(name, default=None):
    # Making decouple first as os.environ can fail on local sometimes.
    try:
        from decouple import config
        return config(name, default)
    except (ImportError, ModuleNotFoundError) as err:
        return os.environ.get(name, default)


def generate_django_key():
    """Generates a secure, random 50-character Django secret key."""
    return f"Django-Secure-Key:{get_random_secret_key()}"
