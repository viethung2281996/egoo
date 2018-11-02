# Activate Django-Heroku.
import dj_database_url
import django_heroku
from egoo_core.settings import INSTALLED_APPS

django_heroku.settings(locals())
db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)

CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

BROKER_URL = os.environ.get("CLOUDAMQP_URL", "django://")
BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_MAX_RETRIES = None

CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]

if BROKER_URL == "django://":
  INSTALLED_APPS += ("kombu.transport.django",)