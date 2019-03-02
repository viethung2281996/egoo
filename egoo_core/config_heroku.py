# Activate Django-Heroku.
import dj_database_url
import django_heroku

django_heroku.settings(locals())
db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)
