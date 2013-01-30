import os, sys

sys.path.append('/home/bob1991/Robotix11/')

sys.path.insert(0, '/home/bob1991/Robotix11')
sys.path.insert(1, '/home/bob1991')


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
