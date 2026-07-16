import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# SECURITY
# ======================================================

# Fallback to local key if environment variable doesn't exist
SECRET_KEY = config('DJANGO_SECRET_KEY', default='django-insecure-^x=5!0fjkvq50f6&5t&ing9=jx=z2sv&x%oi7vfv7v0o9')

DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

# Safe production implementation
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")

# If you prefer to keep using an environment variable for hosts, use this safe fallback:
# env_hosts = os.getenv('DJANGO_ALLOWED_HOSTS')
# ALLOWED_HOSTS = env_hosts.split(',') if env_hosts else ['rlb-am-ems.onrender.com', '127.0.0.1', 'localhost']


# ======================================================
# APPLICATIONS
# ======================================================

INSTALLED_APPS = [
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party Apps
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",

    # Local Apps
    "accounts",
    "dashboard",
    "equipment",
    "rentals",
    "maintenance",
    "fuel",
    "finance",
    "employees",
    "projects",
    "real_estate",
    "crm",
    "reports",
    "documents",
    "notifications",
    "settings_app",
]


# ======================================================
# MIDDLEWARE
# ======================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================================================
# URLS & WSGI
# ======================================================

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"


# ======================================================
# TEMPLATES
# ======================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ======================================================
# DATABASE - Smart Switching (SQLite local, PostgreSQL on Render)
# ======================================================

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT", "5432"),
        }
    }


# ======================================================
# PASSWORD VALIDATION
# ======================================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ======================================================
# INTERNATIONALIZATION
# ======================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Dar_es_Salaam"
USE_I18N = True
USE_TZ = True


# ======================================================
# STATIC FILES
# ======================================================

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ======================================================
# MEDIA
# ======================================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ======================================================
# CRISPY FORMS
# ======================================================

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# ======================================================
# AUTHENTICATION
# ======================================================

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"

AUTH_USER_MODEL = "accounts.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ======================================================
# COMPANY INFORMATION
# ======================================================

COMPANY_NAME = "RLB-AM Construction & Real Estate Ltd"
SYSTEM_NAME = "RLB-AM Enterprise Management System"
SYSTEM_SHORT_NAME = "RLB-AM EMS"


# ======================================================
# PRODUCTION SETTINGS
# ======================================================

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"