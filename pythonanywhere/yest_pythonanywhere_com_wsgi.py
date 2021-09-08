# /var/www/yest_pythonanywhere_com_wsgi.py
# # +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/yest/yest/yest/'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'yest.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
