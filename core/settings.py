import os
import environ
from pathlib import Path
from django.db import backends

env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
APP_URL = os.environ.get('APP_URL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')
API_WHATSAPP_WEB = os.environ.get('API_WHATSAPP_WEB')
HELP_NUMBER = os.environ.get('HELP_NUMBER')

ALLOWED_HOSTS = [
    "arrow.acidjelly.com",
    "www.arrow.acidjelly.com",
    '137.184.230.42',
    '127.0.0.1',
    'localhost'
]

CORS_ORIGIN_WHITELIST = [
    "http://137.184.230.42:4774",
    "http://localhost:3000",
    "https://acidjelly.com"
]

# CSRF_COOKIE_DOMAIN = "acidjelly.com"

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://acidjelly.com"
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.monitoreo',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}

CKEDITOR_UPLOAD_PATH = "/media/"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_DEFAULT_NAME'),
        'USER': os.environ.get('DB_DEFAULT_USER'),
        'PASSWORD': os.environ.get('DB_DEFAULT_PASSWORD'),
        'HOST': os.environ.get('DB_DEFAULT_HOST'),
        'PORT': os.environ.get('DB_DEFAULT_PORT'),
        'OPTIONS': {
            'sslmode': 'disable', # disable SSL
        },
        'DISABLE_SSL': True
    },
    'monitoreo': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_MONITOREO_NAME'),
        'USER': os.environ.get('DB_MONITOREO_USER'),
        'PASSWORD': os.environ.get('DB_MONITOREO_PASSWORD'),
        'HOST': os.environ.get('DB_MONITOREO_HOST'),
        'PORT': os.environ.get('DB_MONITOREO_PORT'),
        'OPTIONS': {
            'sslmode': 'disable', # disable SSL
        },
        'DISABLE_SSL': True
    },
}

DATABASES['default']["ATOMIC_REQUEST"] = True
# DATABASES['cronos']["ATOMIC_REQUEST"] = True
# DATABASES['chatbot']["ATOMIC_REQUEST"] = True
# DATABASES['atlantic_club']["ATOMIC_REQUEST"] = True
# DATABASES['atlantic_seguridad']["ATOMIC_REQUEST"] = True
# DATABASES['atlantic_puntos']["ATOMIC_REQUEST"] = True
# DATABASES['crmcloud']["ATOMIC_REQUEST"] = True
# DATABASES['crm']["ATOMIC_REQUEST"] = True
# DATABASES['bd_games']["ATOMIC_REQUEST"] = True

DATABASE_ROUTERS = [
    'apps.monitoreo.router.MonitoreoRouter',
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 16
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

FILE_UPLOAD_PERMISSIONS = 0o640

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    DJANGO_SERVER_EMAIL = "info@acidjelly.com"
    DEFAULT_FROM_EMAIL = "Acid Jelly <info@acidjelly.com>"
    EMAIL_BACKEND = env('EMAIL_BACKEND')
    
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')
    
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
