"""
Used for deploying
gunicorn --env DJANGO_SETTINGS_MODULE=tinyapp wsgi
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tinyapp')
application = get_wsgi_application()

# vim: ai et ts=4 sw=4 sts=4 nu
