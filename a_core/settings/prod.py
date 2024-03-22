from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    # add your domain here
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
    }
}
