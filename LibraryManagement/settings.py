"""
Django settings for LibraryManagement project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# import os to access environment variables
import os

# import load_dotenv to load environment variables from .env file
from dotenv import load_dotenv

########################################################################
# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# create an empty static directory if it does not exist
if not os.path.exists(os.path.join(BASE_DIR, 'static')):
    os.makedirs(os.path.join(BASE_DIR, 'static'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Save secret key in .env file
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "kcswe.pythonanywhere.com"]


# Application definition
# add LibraryAPI
# Add rest_framework
INSTALLED_APPS = [
    'LibraryAPI',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # add whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryManagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# https://help.pythonanywhere.com/pages/DjangoStaticFiles#set-static_root-in-settingspy
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# more places for collectstatic to find static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# whitenoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# set up cache for throttling
# https://www.django-rest-framework.org/api-guide/throttling/#setting-up-the-cache
# https://docs.djangoproject.com/en/5.1/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'api-throttling',
    }
}

# implement rate limiting with Django's built-in throttling capabilities
# https://www.django-rest-framework.org/api-guide/throttling/#setting-the-throttling-policy
# no authentication required so use AnonRateThrottle
# https://www.django-rest-framework.org/api-guide/throttling/#anonratethrottle
# set the pagination style globally
# https://www.django-rest-framework.org/api-guide/pagination/#setting-the-pagination-style
# https://www.django-rest-framework.org/api-guide/pagination/#setup
# add versioning globally
# https://www.django-rest-framework.org/api-guide/versioning/#configuring-the-versioning-scheme
# https://www.django-rest-framework.org/api-guide/versioning/#other-versioning-settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning', # request.version should return 1
    'DEFAULT_VERSION': 'v1', # DRF expects version numbers without prefixes e.g. 'v', else it would duplicate into /api/vv1/
    'ALLOWED_VERSIONS': ['v1'],
    'VERSION_PARAM': 'version',
}