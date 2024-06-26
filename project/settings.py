import os
from environs import Env


env = Env()
env.read_env()
DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('DB_SECRET_KEY')

DEBUG = env.bool('DEBUG_VALUE', False)

ROOT_URLCONF = 'project.urls'

allowed_hosts_default = ['[::1]', '.localhost', '127.0.0.1']


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', allowed_hosts_default)

                         
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.getenv('DB_LANGUAGE_CODE')

TIME_ZONE = os.getenv('DB_TIME_ZONE')

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
