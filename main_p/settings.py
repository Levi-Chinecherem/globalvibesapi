
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2)^qq@@nn-++p!m_a#36ei9jzi#_q4q*!as9xs!eu^wy=4qohj'

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
    'drf_yasg',
    'rest_framework',
    'accounts', 
    'blog',
    'chat',
    'consultation',
    'moderators',

    'ckeditor',
    'ckeditor_uploader',

    'taggit',

    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',  # Example: Google provider
    # 'allauth.socialaccount.providers.facebook',  # Example: Facebook provider
    # 'allauth.socialaccount.providers.github',  # Example: GitHub provider

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # 'drf_yasg.middleware.SwaggerMiddleware',
]

ROOT_URLCONF = 'main_p.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_p.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Define the root directory for static files.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/root')

# Define the directory where your static files are located.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Define the root directory for media files.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_BASEPATH = "/static/root/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = 'uploads/'  
CKEDITOR_IMAGE_BACKEND = "ckeditor_uploader.backends.PillowBackend"

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'  # Use the appropriate jQuery version
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
# CKEditor jQuery URL
CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'

# CKEditor Uploader settings
CKEDITOR_ALLOW_NONIMAGE_FILES = True  # Disallow non-image file uploads (can be True if needed).
CKEDITOR_RESTRICT_BY_USER = True  # Restrict file uploads to the current user.
CKEDITOR_FILENAME_GENERATOR = 'ckeditor_uploader.utils.get_filename'

# CKEditor Uploader views (optional, for more advanced usage)
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_BROWSE_SHOW_HIDDEN = False
CKEDITOR_BROWSE_SHOW_INFO = True

# CKEditor media settings
CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # Use the correct import based on your Django OAuth Toolkit version
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.BasicAuthentication',  # Include Basic Authentication
        'rest_framework.authentication.SessionAuthentication', 
    ),
}

AUTHENTICATION_BACKENDS = (
    
    'django.contrib.auth.backends.ModelBackend',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Social providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v9.0',
    },
    'github': {
        'SCOPE': ['user'],
        'VERIFIED_EMAIL': False,
    },
}

SOCIALACCOUNT_AUTHENTICATION_METHOD = 'email'

DRFSO2_URL_NAMESPACE = 'rest_framework_social_oauth2'


# Specify the custom user model for the accounts app
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Set the desired page size
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
