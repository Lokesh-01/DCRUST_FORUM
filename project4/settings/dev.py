from .base import *
import dj_database_url

SECRET_KEY = '13kl@xtukpwe&xj2xoysxe9_6=tf@f8ewxer5n&ifnd46+6$%8'
DEBUG = True
ALLOWED_HOSTS = ['dcrustforum.herokuapp.com','127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES = { 'default': dj_database_url.config(conn_max_age=500) }
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'