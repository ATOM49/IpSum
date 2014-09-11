"""
Django settings for webProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_DIRS = os.path.join(BASE_DIR, "templates")
STATIC_PATH = os.path.join(PROJECT_PATH,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au*b^+m&z_fjn!@9s3#%lyv_m)083(gsyeydw^ucezlpo37lim'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'guardian',
    'south',
    'shops',
    'products',
    'users',
    'core',
    'crispy_forms',
    'pagination',
    'django_facebook',
    'waypoints',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    # 'django_facebook.context_processors.facebook',
)

ANONYMOUS_USER_ID = -1
AUTHENTICATION_BACKENDS = (
    # 'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)


ROOT_URLCONF = 'IpSum.urls'

WSGI_APPLICATION = 'IpSum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


#sqlite3 config
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "ipsum",
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': ''
    }
}

#GEOS_LIBRARY_PATH = r'C:\OSGeo4W64\bin'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/static/"
LOGIN_URL = '/users/login/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'


#Custom User Profile AUTH settings
AUTH_PROFILE_MODULE= 'users.UserProfile'


#Facebook Initialzation
# FACEBOOK_APP_ID = '637419996372962'
# FACEBOOK_APP_SECRET = '7d56623819e89c6f5671f7b456f5d3f8'
# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'