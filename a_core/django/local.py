from .base import *  # noqa: F403

MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN=True

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MFA_TOTP_ISSUER = "Demo app"

ALLOWED_HOSTS        = ['localhost', 'localhost:85', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1']