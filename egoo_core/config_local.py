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

# Cloudinary settings for Django. Add to your settings file.
cloudinary.config(
  cloud_name = 'egoodev',  
  api_key = '968886895255698',  
  api_secret = 'RvrscTeNAfWtshM-ftDpclOFF5I',  
)