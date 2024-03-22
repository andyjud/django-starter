"""
WSGI config for a_core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a_core.settings")

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


application = get_wsgi_application()
