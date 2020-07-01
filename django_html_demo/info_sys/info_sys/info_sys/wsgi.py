"""
WSGI config for info_sys project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "info_sys.settings")

application = get_wsgi_application()
