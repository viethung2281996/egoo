import dj_database_url
import django_heroku
import cloudinary

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'egoo_core',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    'PORT': '3306',
  }
}

django_heroku.settings(locals())
db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Cloudinary settings for Django. Add to your settings file.
cloudinary.config(
  cloud_name = 'egoodev',  
  api_key = '968886895255698',  
  api_secret = 'RvrscTeNAfWtshM-ftDpclOFF5I',  
)