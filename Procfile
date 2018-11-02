
web: gunicorn egoo_core.wsgi --log-file -
worker: celery -A egoo_core worker -B -l INFO