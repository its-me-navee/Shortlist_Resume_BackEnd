import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shortlist_Resume_BackEnd.settings')

application = get_asgi_application()