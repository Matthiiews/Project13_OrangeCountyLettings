import os
import sentry_sdk
import environ
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# take environment variables from .env
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', default='default_local_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG_VALUE', default=False)

SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LETTING_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'lettings.apps.LettingsConfig',
    'profiles.apps.ProfilesConfig',
]

INSTALLED_APPS = LETTING_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DATABASE_NAME = os.environ.get('DJANGO_DATABASE_NAME', 'default_db_name')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.environ.get('DJANGO_DATABASE_NAME') + '.sqlite3'),
    }
}

# DOCKER_USERNAME = os.environ.get('DOCKER_USERNAME')
# DOCKER_PASSWORD = os.environ.get('DOCKER_PASSWORD')
# EC2_HOST = os.environ.get('EC2_HOST')
# EC2_USERNAME = os.environ.get('EC2_USERNAME')
# EC2_SECRET_KEY = os.environ.get('EC2_SECRET_KEY')

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# Static file serving.
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static", ]

# Settings for Sentry
try:
    DSN_SENTRY = os.environ['DSN_SENTRY']
except KeyError:
    DSN_SENTRY = ''

sentry_sdk.init(
    dsn=DSN_SENTRY,
    integrations=[
        DjangoIntegration(
            transaction_style="url",
            middleware_spans=True,
            signals_spans=False,
            cache_spans=False,
        )
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    send_default_pii=True
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {module} {message}",
            'datefmt': '%Y-%m-%d %H:%M:%S',
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    'handlers': {
        'console': {
            "level": "DEBUG",
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            "level": "DEBUG",
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'when': 'midnight',  # Rotate logs at midnight
            'backupCount': 7,    # Keep logs for 7 days
            'formatter': 'verbose'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'sentry_sdk.integrations.logging.EventHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        'lettings': {
            'handlers': ['file', 'console', 'sentry'],
            'level': 'DEBUG',
        },
        'profiles': {
            'handlers': ['file', 'console', 'sentry'],
            'level': 'INFO',
        }
    },
}

DEBUG_PROPAGATE_EXCEPTIONS = True
