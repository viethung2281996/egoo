import cloudinary
from egoo_core.settings import INSTALLED_APPS
import os

# Cloudinary settings for Django. Add to your settings file.
cloudinary.config(
  cloud_name = 'egoodev',  
  api_key = '968886895255698',  
  api_secret = 'RvrscTeNAfWtshM-ftDpclOFF5I',  
)

CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

BROKER_URL = os.environ.get("CLOUDAMQP_URL", "django://")
BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_MAX_RETRIES = None

CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]

if BROKER_URL == "django://":
  INSTALLED_APPS += ("kombu.transport.django",)