from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'casaarbol',
        'USER':'postgres',
        'PASSWORD':'sgm881',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')