"""
Django settings for newsportal_project project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1bi0ja2y%=xsyp23o#4ool(4lk5=+p@8#!w%-t-_eaxf&k-t7-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'newsportal_app',
    'newsportal_app.apps.NewsportalAppConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'django_apscheduler',
    'allauth',                                          #для подключения allauth модуль D5.4
    'allauth.account',                                  #для подключения allauth модуль D5.4
    'allauth.socialaccount',                            #для подключения allauth модуль D5.4
    'allauth.socialaccount.providers.yandex',           #для подключения allauth модуль D5.4

]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'newsportal_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',                   #для подключения allauth модуль D5.4
                ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',                    #для подключения allauth модуль D5.4
    'allauth.account.auth_backends.AuthenticationBackend',          #для подключения allauth модуль D5.4
]

WSGI_APPLICATION = 'newsportal_project.wsgi.application'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
SITE_URL = 'http://127.0.0.1:8080'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

ACCOUNT_EMAIL_REQUIRED = True                        #для подключения allauth модуль D5.4
ACCOUNT_UNIQUE_EMAIL = True                         #для подключения allauth модуль D5.4
ACCOUNT_USERNAME_REQUIRED = False                   #для подключения allauth модуль D5.4
ACCOUNT_AUTHENTICATION_METHOD = 'email'             #для подключения allauth модуль D5.4
ACCOUNT_EMAIL_VERIFICATION = 'none'                 #для подключения allauth модуль D5.4

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignUpForm"}   #Модуль D5.4

LOGIN_REDIRECT_URL = "/news"

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же           #модуль D6.2
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый                                        #модуль D6.2
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')                                                            #модуль D6.2
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')                                                     #модуль D6.2
EMAIL_USE_SSL = True                                                                         #модуль D6.2
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LOGGING = {
    'version': 1,
    'disable_existing_logging': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)-24s %(levelname)-8s %(message)s',
        },
        # console&mail
        'warning': {
            'format': '{asctime} -- {levelname} -- {message} --> {pathname}',
            'style': '{',
        },
        # console&file errors
        'error': {
            'format': '{asctime} -- {levelname} -- {message} --> {pathname} *** {exc_info}',
            'style': '{',
        },
        # security&general
        'file': {
            'format': '{asctime} -- {levelname} -- {message} -- {module}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error'
        },
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'general.log'
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': 'errors.log'
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'security.log'
        },
        'mail': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'warning',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'file'],
            'propagate': True,
            'level': 'DEBUG'
        },
        'django.request': {
            'handlers': ['file_errors', 'mail'],
            'propagate': True
        },
        'django.server': {
            'handlers': ['file_errors', 'mail'],
            'propagate': True
        },
        'django.template': {
            'handlers': ['file_errors'],
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'propagate': True
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True
        }
    }
}