import os

from django.core.asgi import get_asgi_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = get_asgi_app()
