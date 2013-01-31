# Django settings for Robotix13 project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dementor', 'soumyadeep@robotix.in'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'robotix13',
        'USER': 'root',
        'PASSWORD': 'sushmita',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = None
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

# Not needed
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = '/var/www/media'

MEDIA_URL = 'http://10.102.43.231/media'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'fs6f)h#+hk+m*pi_(oj2vbd_sl9dc8)0i$pw1(&ycnhh7#ht4!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'rbtxportal.urls'

TEMPLATE_DIRS = (
    '/home/dementor/rbtxportal/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'rbtxportal.eventmanager',
)
