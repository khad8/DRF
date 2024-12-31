from pathlib import Path
from datetime import timedelta
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#h_p6y5kav03-p#(f4ylp@x+r^$ds)+8e&ptwe&xgd8$@vl$$b'

DEBUG = True

ALLOWED_HOSTS = ["*"]


STATIC_URL = 'https://s3.erp-beast.com/wa-academy/static'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") # IT SHOULD BE IGNORED BY DJANGO

# MinIO Configuration Using "django-storages"
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": "SoVaSe71NqoGOpZx0uVb",
            "secret_key": "67rGMwbYxExyicmbjyFbDw0e7zmNbuqzvc9OsGz4",
            "bucket_name": "chikh",
            "endpoint_url": "https://s3.erp-beast.com",
            "region_name": None,  # MinIO does not require a region
            "default_acl": "public-read",
            "querystring_auth": False,  # Change to True if you want querystring authentication
            "object_parameters": {
                "CacheControl": "max-age=86400",
            },
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": "SoVaSe71NqoGOpZx0uVb",
            "secret_key": "67rGMwbYxExyicmbjyFbDw0e7zmNbuqzvc9OsGz4",
            "bucket_name": "wa-academy",
            "endpoint_url": "https://s3.erp-beast.com",
            "region_name": None,
            "default_acl": "public-read",
            "object_parameters": {
                "CacheControl": "max-age=86400",
            },
        },
    },
}

DEFAULT_FILE_STORAGE = "storages.backends.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3.S3Storage"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # THIRD PARTY APPS
    'rest_framework',
    # CUSTOM APPS
    'api',
]

REST_FRAMEWORK = {
    # Force users to be authenticated to use the ressources
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    # jwt as default auth class
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": [
        # Enforce the response to be JSON
        "rest_framework.parsers.JSONParser",
        # Use the Forms
        "rest_framework.parsers.FormParser",
        # Use of files / media
        "rest_framework.parsers.MultiPartParser"
    ]
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=45),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drfdemo.urls'

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

WSGI_APPLICATION = 'drfdemo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
