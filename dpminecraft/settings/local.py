"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to dpminecraft/settings/local.py. It should not be checked into
your code repository.

"""
from dpminecraft.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ash', 'ash@dragonpaw.org'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

# ROOT_URLCONF = 'dpminecraft.urls.local'
# WSGI_APPLICATION = 'dpminecraft.wsgi.local.application'
