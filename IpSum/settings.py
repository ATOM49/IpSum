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
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au*b^+m&z_fjn!@9s3#%lyv_m)083(gsyeydw^ucezlpo37lim'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = (
    '*')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'shops',
    'products',
    'users',
    'core',
    'crispy_forms',
    'pagination',
    'social_auth'
    # 'django_facebook',
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
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'

ANONYMOUS_USER_ID = -1
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'guardian.backends.ObjectPermissionBackend',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'IpSum.urls'

WSGI_APPLICATION = 'IpSum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
'''
DATABASES = {
    'default': {S
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "ipsum",
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': ''
    }
}

#GEOS_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal110.dll'
'''

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
LOGIN_URL = '/core/login/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/core/register/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/users/home/'
MEDIA_URL = '/media/'


#Custom User Profile AUTH settings
AUTH_PROFILE_MODULE= 'users.UserProfile'
FACEBOOK_AUTH_PROFILE_MODULE= 'users.FacebookProfile'

#Facebook Initialzation
FACEBOOK_APP_ID = '637419996372962'
FACEBOOK_API_SECRET = '7d56623819e89c6f5671f7b456f5d3f8'
# FACEBOOK_AUTH_USER_MODEL = 'django_facebook.models.FacebookProfileModel'
# FACEBOOK_AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
FACEBOOK_DEFAULT_SCOPE = ['email', 'user_birthday', 'user_website', 'user_friends']
FACEBOOK_STORE_LIKES = True
FACEBOOK_STORE_FRIENDS = True

#Twilio details
TWILIO_ACCOUNT_SID = "AC9dbcad82b20275e6e1854351444f13c3"
TWILIO_AUTH_TOKEN = "d5eb94487e911314e5620b4ea18e6d74"
TWILIO_FROM_NUMBER = "(717) 833-6007"
default_client = 'anonymous'

#Pusher details
p_key = 'fc3f7ce5a53bc331ec26'
p_secret = 'ce2ddcccec20e0ecd5a3'
p_app_id = '89743'