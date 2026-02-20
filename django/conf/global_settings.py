#
# This is the Django settings file for the project.
#
# It's sourced by the ``django.conf.settings`` object, which is the
# Django settings object.  It's used by the ``django.conf`` module to
# provide a central place to store configuration data.
#
# See the ``django.conf`` module documentation for more information.
#
# NOTE: This file is sourced by the ``django.conf.settings`` object.
#       Do not import this file directly.
#

import os
import time
from pathlib import Path

# The ``BASE_DIR`` is the directory containing the Django project.
# It's used to locate the project's static files, templates, etc.
BASE_DIR = Path(__file__).resolve().parent.parent

# The ``SECRET_KEY`` is used for cryptographic signing.
# It's a randomly generated string that's used to sign
# session cookies, CSRF tokens, and other security-related data.
SECRET_KEY = 'django-insecure-placeholder-key-for-development-only'

# The ``DEBUG`` setting controls whether Django runs in debug mode.
# When ``True``, Django will display detailed error pages and
# will serve static files.  When ``False``, Django will display
# generic error pages and will not serve static files.
DEBUG = True

# The ``ALLOWED_HOSTS`` setting controls which hostnames Django
# will respond to.  It's a list of strings, where each string is
# a hostname that Django will respond to.
ALLOWED_HOSTS = []

# The ``INSTALLED_APPS`` setting controls which Django applications
# are installed in the project.  It's a list of strings, where each
# string is the name of a Django application.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# The ``MIDDLEWARE`` setting controls which middleware classes
# are used by Django.  It's a list of strings, where each string is
# the path to a middleware class.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'modern_data_pipeline_rl5f.urls'

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

WSGI_APPLICATION = 'modern_data_pipeline_rl5f.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
