import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a_core.settings")

celery_app = Celery("a_core")
celery_app.config_from_object("django.conf.settings", namespace="CELERY")
celery_app.autodiscover_tasks()
# Import the celery app in init.py to ensure it's loaded when Django starts.
