"""Django settings for manager project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
from typing import Any, Dict, Sequence, Tuple
import dj_database_url

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY: str = "z6*^gkyb6avt*dzc30k7a8qqq(x6_!t2%3wor$h%38*i+#(jne"
DEBUG: bool = True
ALLOWED_HOSTS: Sequence[str] = (
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "quote-quote.herokuapp.com",
)
INSTALLED_APPS: Sequence[str] = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_registration",
    "rest_framework",
    "drf_yasg",
    "app",
    "api",
)
MIDDLEWARE: Sequence[str] = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
ROOT_URLCONF: str = "manager.urls"
TEMPLATES: Tuple[Any] = (
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "manager/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
)
WSGI_APPLICATION: str = "manager.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES: Dict[str, Dict[str, str]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: Sequence[Dict[str, str]] = (
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation."
        "CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "NumericPasswordValidator"
    },
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL: str = "/static/"
PROJECT_ROOT: str = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS: Tuple[str, ...] = (os.path.join(PROJECT_ROOT, "static"),)
STATIC_ROOT: str = os.path.join(PROJECT_ROOT, "staticfiles")
STATICFILES_STORAGE: str = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)
DATABASES["default"].update(dj_database_url.config(conn_max_age=500))

ACCOUNT_ACTIVATION_DAYS: int = 7  # amount of days for link to be activated
LOGOUT_REDIRECT_URL: str = "quotes:quotes"
LOGIN_REDIRECT_URL: str = "quotes:quotes"

EMAIL_HOST: str = "smtp.sendgrid.net"
EMAIL_PORT: int = 587
EMAIL_USE_TLS: bool = True
EMAIL_HOST_USER: str = ""
EMAIL_HOST_PASSWORD: str = ""

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}
