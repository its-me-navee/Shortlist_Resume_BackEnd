import os

from django.core.wsgi import get_wsgi_application

settings_module = 'Shortlist_Resume_BackEnd.production' if 'WEBSITE_HOSTNAME' in os.environ else 'cv-shortlister-backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
