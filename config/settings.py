import os
from pathlib import Path
from decouple import config
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent



# ======================================================
# SECURITY & ENVIRONMENT
# ======================================================

SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="django-insecure-change-this-key"
)


DEBUG = config(
    "DJANGO_DEBUG",
    default=True,
    cast=bool
)


ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost"
).split(",")



if not DEBUG:

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    CSRF_TRUSTED_ORIGINS = config(
        "CSRF_TRUSTED_ORIGINS",
        default=""
    ).split(",")





# ======================================================
# APPLICATIONS
# ======================================================


INSTALLED_APPS = [


    # Django Core

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    "django.contrib.humanize",



    # Third Party

    "crispy_forms",

    "crispy_bootstrap5",

    "django_filters",

    "widget_tweaks",

    "whitenoise.runserver_nostatic",



    # Local Apps

    "accounts",

    "core",

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
# URL CONFIGURATION
# ======================================================


ROOT_URLCONF = "config.urls"


WSGI_APPLICATION = "config.wsgi.application"







# ======================================================
# TEMPLATES
# ======================================================


TEMPLATES = [


    {

        "BACKEND":
        "django.template.backends.django.DjangoTemplates",


        "DIRS":
        [
            BASE_DIR / "templates"
        ],


        "APP_DIRS":
        True,


        "OPTIONS":

        {

            "context_processors":

            [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",


                "core.context_processors.sidebar_menu",

                "core.context_processors.company_info",

            ],

        },

    },

]







# ======================================================
# DATABASE
# ======================================================


if DEBUG:


    DATABASES = {


        "default":

        {


            "ENGINE":
            "django.db.backends.sqlite3",


            "NAME":
            BASE_DIR / "db.sqlite3",

        }

    }



else:


    DATABASES = {


        "default":

        {


            "ENGINE":
            "django.db.backends.postgresql",


            "NAME":
            config("DATABASE_NAME"),


            "USER":
            config("DATABASE_USER"),


            "PASSWORD":
            config("DATABASE_PASSWORD"),


            "HOST":
            config("DATABASE_HOST"),


            "PORT":
            config(
                "DATABASE_PORT",
                default="5432"
            ),


            "ATOMIC_REQUESTS":
            True,


            "CONN_MAX_AGE":
            600,

        }

    }








# ======================================================
# AUTHENTICATION
# ======================================================


AUTH_USER_MODEL = "accounts.User"


LOGIN_URL = "accounts:login"


LOGIN_REDIRECT_URL = "dashboard:dashboard"


LOGOUT_REDIRECT_URL = "accounts:login"




SESSION_COOKIE_AGE = 604800


SESSION_SAVE_EVERY_REQUEST = True


SESSION_EXPIRE_AT_BROWSER_CLOSE = False


SESSION_COOKIE_HTTPONLY = True







AUTH_PASSWORD_VALIDATORS = [


    {

        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator"

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator"

    },


    {

        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator"

    },

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


STATIC_URL = "/static/"


STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_DIRS = [

    BASE_DIR / "static"

]


STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)






# ======================================================
# MEDIA FILES
# ======================================================


MEDIA_URL = "/media/"


MEDIA_ROOT = BASE_DIR / "media"






FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880


DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760








# ======================================================
# CRISPY FORMS
# ======================================================


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


CRISPY_TEMPLATE_PACK = "bootstrap5"







# ======================================================
# EMAIL
# ======================================================


EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)


EMAIL_HOST = config(
    "EMAIL_HOST",
    default="smtp.gmail.com"
)


EMAIL_PORT = 587


EMAIL_USE_TLS = True


EMAIL_HOST_USER = config(
    "EMAIL_HOST_USER",
    default=""
)


EMAIL_HOST_PASSWORD = config(
    "EMAIL_HOST_PASSWORD",
    default=""
)


DEFAULT_FROM_EMAIL = (
    "RLB-AM EMS"
)







# ======================================================
# MESSAGES
# ======================================================


MESSAGE_TAGS = {


    messages.DEBUG:
    "secondary",


    messages.INFO:
    "info",


    messages.SUCCESS:
    "success",


    messages.WARNING:
    "warning",


    messages.ERROR:
    "danger",

}







# ======================================================
# COMPANY INFORMATION
# ======================================================


COMPANY_NAME = (
    "RLB-AM Construction & Real Estate Ltd"
)


SYSTEM_NAME = (
    "RLB-AM Enterprise Management System"
)


SYSTEM_SHORT_NAME = (
    "RLB-AM EMS"
)


SYSTEM_VERSION = "1.0.0"







# ======================================================
# DEFAULT PRIMARY KEY
# ======================================================


DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)