import environ
from .base import *  # base에 있는 모든 내용을 사용한다. ALLOWED_HOSTS만 따로 사용한다.

ALLOWED_HOSTS = ['52.78.201.179'] #AWS 고정  IP
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

env = environ.Env()
environ.Env.read_env(BASE_DIR/'.env')

DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': env('DB_NAME'),
		'USER': env('DB_USER'),
		'PASSWORD': env('DB_PASSWORD'),
		'HOST': env('DB_HOST'),
		'PORT': '3306',
    }
}