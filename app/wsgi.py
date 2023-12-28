"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = get_wsgi_app()
