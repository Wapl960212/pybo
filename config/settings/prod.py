from .base import *  # base에 있는 모든 내용을 사용한다. ALLOWED_HOSTS만 따로 사용한다.

ALLOWED_HOSTS = ['3.38.56.241'] #AWS 고정  IP
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []