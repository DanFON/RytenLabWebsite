"""
Django settings for braineacv2 project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'setp.gmail.com'
EMAIL_HOST_USER = 'danielfoonah@gmail.com'
EMAIL_HOST_PASSWORD = 'your gmail password'
EMAIL_PORT ='587'
EMAIL_USE_TLS =True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@0lqz))-9rd!+b$cb07z&*+p=&k(m6guqu$=r(=axhpcj*(cok'

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
    'contact',
    'contact_us',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'resources',
    # 'profile',
    
    
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

ROOT_URLCONF = 'braineacv2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'braineacv2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static','static')
    MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')

    STATICFILES_DIRS =(
    os.path.join(BASE_DIR, 'static','static-only'),
  
)

# STATIC_URL = '/static'

# STATIC_ROOT = os.path.join(BASE_DIR,'static', 'static_root')

# STATICFILES_DIRS= (
#     os.path.join(BASE_DIR, 'static', 'static_dirs')
# )

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

# MEDIA_URL = '/media'



CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email' 
ACCOUNT_EMAIL_REQUIRED = False 
ACCOUNT_CONFIRM_EMAIL_ON_GET =False 

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL 
 
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None 

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3 

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True 
 
ACCOUNT_EMAIL_REQUIRED =False 

ACCOUNT_EMAIL_VERIFICATION =None 

ACCOUNT_EMAIL_SUBJECT_PREFIX ='My subject: ' 

ACCOUNT_DEFAULT_HTTP_PROTOCOL ='http' 

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN =180 
 
ACCOUNT_FORMS ={} 

ACCOUNT_LOGIN_ATTEMPTS_LIMIT =5 
 
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300 

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True 

ACCOUNT_LOGOUT_ON_GET =False 

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =False 

ACCOUNT_LOGIN_ON_PASSWORD_RESET =False 

ACCOUNT_LOGOUT_REDIRECT_URL ='/'

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False 
ACCOUNT_PASSWORD_MIN_LENGTH = 6

ACCOUNT_PRESERVE_USERNAME_CASING =True 

ACCOUNT_SESSION_REMEMBER =None 

ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE =False 
 
ACCOUNT_SIGNUP_FORM_CLASS =None 

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =True 

ACCOUNT_TEMPLATE_EXTENSION ='html' 

ACCOUNT_USERNAME_BLACKLIST =[] 

ACCOUNT_UNIQUE_EMAIL =True 

#ACCOUNT_USER_DISPLAY ='username' 

ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username' 
 
ACCOUNT_USERNAME_MIN_LENGTH =5 

ACCOUNT_USERNAME_REQUIRED =True 

ACCOUNT_USERNAME_VALIDATORS =None


