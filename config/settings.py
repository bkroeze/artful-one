import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET") or "dev-secret-s(p7%ue-l6r^&@y63p*ix*1"
SCREENSHOT_SECRET = os.environ.get("SCREENSHOT_SECRET") or ""


# Helpers
def env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def env_list(name: str, default: list[str] | None = None) -> list[str]:
    value = os.environ.get(name)
    if value is None:
        return default or []
    return [item.strip() for item in value.split(",") if item.strip()]


# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_bool("DJANGO_DEBUG")
INTERNAL_IPS = ("127.0.0.1",)

STAGING = env_bool("STAGING")

# Cloudflare details
CLOUDFLARE_EMAIL = os.environ.get("CLOUDFLARE_EMAIL", "")
CLOUDFLARE_TOKEN = os.environ.get("CLOUDFLARE_TOKEN", "")
CLOUDFLARE_ZONE_ID = os.environ.get("CLOUDFLARE_ZONE_ID", "")

# Mailgun contact form delivery
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY", "")
MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN", "")
MAILGUN_API_URL = os.environ.get("MAILGUN_API_URL", "https://api.mailgun.net/v3")
MAILGUN_FROM_EMAIL = os.environ.get(
    "MAILGUN_FROM_EMAIL",
    f"Artful.One Contact <postmaster@{MAILGUN_DOMAIN}>" if MAILGUN_DOMAIN else "",
)
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "")

# https://github.com/simonw/simonwillisonblog/issues/498
SECURE_CROSS_ORIGIN_OPENER_POLICY = "unsafe-none"

# SESSION_COOKIE_DOMAIN
if os.environ.get("SESSION_COOKIE_DOMAIN"):
    SESSION_COOKIE_DOMAIN = os.environ["SESSION_COOKIE_DOMAIN"]
if os.environ.get("SESSION_COOKIE_SECURE"):
    SESSION_COOKIE_SECURE = env_bool("SESSION_COOKIE_SECURE")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_hosts",
    "blog",
    "monthly",
    "feedstats",
    "filedrop",
    "pictures",
    "rpg",
    "rpg_chargen",
    "sketches",
    "django_http_debug",
    "pixelborders.apps.PixelbordersConfig",
    "sigils",
]

MIDDLEWARE = [
    "config.healthcheck.HealthCheckMiddleware",
    "django_hosts.middleware.HostsRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_http_debug.middleware.DebugMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "blog.middleware.AmpersandRedirectMiddleware",
    "django_hosts.middleware.HostsResponseMiddleware",
]
if DEBUG:
    try:
        MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
        INSTALLED_APPS += ["debug_toolbar"]
    except ImportError:
        pass

# Sentry
SENTRY_DSN = os.environ.get("SENTRY_DSN")
if SENTRY_DSN:
    INSTALLED_APPS += ("raven.contrib.django.raven_compat",)
    RAVEN_CONFIG = {
        "dsn": SENTRY_DSN,
        "release": os.environ.get("HEROKU_SLUG_COMMIT", ""),
    }


ROOT_URLCONF = "config.urls"
ROOT_HOSTCONF = "config.hosts"
DEFAULT_HOST = "www"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog.context_processors.all",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "artful-one.db",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

if "DATABASE_URL" in os.environ:
    # Parse database configuration from $DATABASE_URL
    DATABASES["default"] = dj_database_url.config()
    DATABASES["dashboard"] = dj_database_url.config()
    # DATABASES["dashboard"]["OPTIONS"] = {
    #     "options": "-c default_transaction_read_only=on -c statement_timeout=3000"
    # }

if "DISABLE_AUTOCOMMIT" in os.environ:
    DATABASES["default"]["AUTOCOMMIT"] = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", ["*"])

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, "staticfiles"))
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
    ("photos", os.path.join(BASE_DIR, "photos")),
)

# Media files (user-uploaded content)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# urls.W002
# Your URL pattern '^/?archive/(\d{4})/(\d{2})/(\d{2})/$' has a regex beginning
# with a '/'. Remove this slash as it is unnecessary. If this pattern is
# targeted in an include(), ensure the include() pattern has a trailing '/'.
# This is deliberate (we get hits to //archive/ for some reason) so I'm
# silencing the warning:
SILENCED_SYSTEM_CHECKS = ("urls.W002",)


# Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "pictures": {
            "handlers": ["console"],
            "level": os.getenv("PICTURES_LOG_LEVEL", "DEBUG"),
            "propagate": False,
        },
        "blog": {
            "handlers": ["console"],
            "level": os.getenv("BLOG_LOG_LEVEL", "DEBUG"),
            "propagate": False,
        },
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        "django.contrib.auth": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "django.security.csrf": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.middleware.csrf": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

PICTURES = {
    "BREAKPOINTS": {
        "xs": 576,
        "s": 768,
        "m": 992,
        "l": 1200,
        "xl": 1400,
    },
    "GRID_COLUMNS": 12,
    "CONTAINER_WIDTH": 1200,
    "FILE_TYPES": ["AVIF"],
    "PIXEL_DENSITIES": [1, 2],
    "USE_PLACEHOLDERS": False,
    "QUEUE_NAME": "pictures",
    "PROCESSOR": "pictures.tasks.process_picture",
}

# Filedrop configuration
FILEDROP_BASE_DIR = os.environ.get(
    "FILEDROP_BASE_DIR", os.path.join(BASE_DIR, "filedrop_files")
)

# Django Tasks configuration for django-pictures
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.immediate.ImmediateBackend",
        "QUEUES": ["pictures"],
    }
}
