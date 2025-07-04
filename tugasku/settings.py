"""
Django settings for tugasku project.
Generated by 'django-admin startproject' using Django 5.1.7.
"""

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-b&um#gnqq$ehes29#wld-da@ki95_hg$1mp-p7hp4zv68^rutv'
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'django-production-c672.up.railway.app',
]

CSRF_TRUSTED_ORIGINS = ['https://django-production-c672.up.railway.app',]

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'artikel',
    'django_ckeditor_5',
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'undo', 'redo',
            '|', 'heading',
            '|', 'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', 'highlight',
            '|', 'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor',
            '|', 'alignment', 'outdent', 'indent', 'removeFormat',
            '|', 'bulletedList', 'numberedList', 'todoList',
            '|', 'link', 'blockQuote', 'code', 'codeBlock',
            '|', 'insertTable', 'imageUpload', 'mediaEmbed', 'htmlEmbed',
            '|', 'horizontalLine', 'specialCharacters', 'pageBreak', 'findAndReplace',
            '|', 'sourceEditing'
        ],
        'language': 'id',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tugasku.urls'

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

WSGI_APPLICATION = 'tugasku.wsgi.application'

# Database config: Railway PostgreSQL or local SQLite fallback
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'