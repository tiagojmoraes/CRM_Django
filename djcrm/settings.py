from pathlib import Path
# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# DEBUG = config('DEBUG')
# SECRET_KEY = config('SECRET_KEY')

DEBUG=True
# SECRET_KEY='django-insecure-d4d9ch7wro5$qqwg+05$h$=jh3o_@c#kgvi4by9e8727!65sk_'
SECRET_KEY="8_&iveva&@=zgb7k(2#ylygze6g04&5gyk@58vgg@3ha^vu6@x"

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    #Third party apps
    'crispy_forms',
    'crispy_tailwind',
    #Local apps
    'leads',
    'agents',    
]

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

ROOT_URLCONF = 'djcrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'djcrm.wsgi.application'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': config("DB_NAME"),
        # 'USER': config("USER"),
        # 'PASSWORD': config("PASSWORD"),
        # 'HOST': config("HOST"),
        # 'PORT': config("PORT"),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'djcrm',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
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

AUTHENTICATION_BACKENDS = [
    'djcrm.backends.EmailOrUsernameBackend'
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# STATIC_ROOT = "static_root"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'leads.User'
LOGIN_REDIRECT_URL = "/leads"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = "/"

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = 'tailwind'

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PHOTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000 # 1 YEAR
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = "DENY"

    ALLOWED_HOSTS = ["*"]

    # EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    # EMAIL_HOST = config("EMAIL_HOST")
    # EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    # EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    # EMAIL_USE_TLS = config("EMAIL_USE_TLS")
    # EMAIL_PORT = config("EMAIL_PORT")
    # DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
    
