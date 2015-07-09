"""
Django settings for documentos project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^8@#&52i=9odrdi97%(-!z+(aa77st2py(gmt@xui^iw&t!5m#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model_utils',
    'django_extensions',

    'simple_history',
    'debug_toolbar',
    'crispy_forms',
    'bootstrap_pagination',
    'core',
    'redactor',
    'django_summernote',
    'autoadmin',
    'sequence_field',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'documentos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'documentos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_producao')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTOADMIN_USERNAME = 'admin'

AUTOADMIN_EMAIL = 'admin@admin.com'

AUTOADMIN_PASSWORD = 'admin'



REDACTOR_OPTIONS = {'lang': 'pt_br', 'plugins': ['video', 'fullscreen']}

REDACTOR_UPLOAD_HANDLER = 'redactor.handlers.UUIDUploader'

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    'height': '480',

    # Use proper language setting automatically (default)
    'lang': None,

    # Or, set editor language/locale forcely
    #'lang': 'ko-KR',

    # Customize toolbar buttons
    # 'toolbar': [
    #     ['style', ['style']],
    #     ['style', ['bold', 'italic', 'underline', 'clear']],
    #     ['para', ['ul', 'ol', 'height']],
    #     ['insert', ['link']],
    # ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': False,

    # Set `upload_to` function for attachments.
    #'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    #'attachment_storage_class': 'my.custom.storage.class.name',

    # Set external media files for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    # 'inplacewidget_external_css': (
    #     '//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css',
    #     '//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css',
    # ),
    # 'inplacewidget_external_js': (
    #     '//code.jquery.com/jquery-1.9.1.min.js',
    #     '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',
    # ),
}