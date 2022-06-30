#!/jiselab.jp/public_html/kotonoha/NILpro_Hist/myenv/lib/python3.9
# encoding: utf-8

import sys, os

sys.path.append("/jiselab.jp/public_html/kotonoha/NILpro_Hist/")

os.environ['DJANGO_SETTINGS_MODULE'] = "pj_db.settings"

from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)