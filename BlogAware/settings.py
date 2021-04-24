"""
Django settings for BlogAware project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '425z)^lt65okkfs($tl7%@23l*#7w&(_16tu^dr*rtgqj9@hc)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BlogApp',
    'ckeditor',
]






MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BlogAware.urls'

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

WSGI_APPLICATION = 'BlogAware.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True




MESSAGES_TAGS={
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)
STATIC_URL = '/static/'


MEDIA_URL=  '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')


#SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "blogaware.dee@gmail.com"
EMAIL_HOST_PASSWORD = "Blog Anna"






##### CKeditor configurations
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'format_tags' : 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
    'default': {
        'removePlugins': ['elementspath',],
        
        
        'toolbar_Basic': [
            ['Bold', 'Italic']
        ],
         'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow',],
            'default' :{'width': "100%"}
        },
        
        

        'toolbar_YourCustomToolbarConfig': [
            
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike','-', 'Subscript', 'Superscript']},
            
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name':'listing','items':['NumberedList', 'BulletedList', 'Indent', 'Outdent']},

            {'name': 'paragraph',
             'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Find', 'Replace']},
            {'name': 'insert',
             'items': ['Link','Image','Table', '-','HorizontalRule','Smiley', 'SpecialChar']}, # 'Iframe','PageBreak' can be added in insert list 
            
            {'name': 'styles', 'items': ['Styles','Font', 'FontSize','CopyFormatting','-','Templates','-','Blockquote']},    #'Format'  can be added
            {'name':'other','items':['Undo','Redo','Print','Maximize',]}
            
            

        ],
        
        'toolbar': 'YourCustomToolbarConfig', 
        'width':'100%' ,
        
        'height' : 'auto',
        
        
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', 
            'div',
            'format',
            'richcombo',
            #'maximize',
            'autolink',
            'autoembed',
            'embedsemantic',
            #'autogrow',
            #'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'wsc',
            'codesnippet',
            #'elementspath'
        ]),
        #'toolbarLocation':'bottom'
    },
   
}
