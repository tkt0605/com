"""
WSGI config for com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the directory containing your Django project to the PYTHONPATH
sys.path.append('/Users/takat/Sites/com')
SECRET_KEY = os.environ.get('django-insecure-r##_c1uam@76#1pn2mww6qc4(xl^q)zm4@z(2lcr&lf&1c7k$&')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "com.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
