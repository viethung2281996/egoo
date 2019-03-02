import datetime
import csv
import zlib
from egoo_core.celery import app
from categories.models import Category
from user.models import UserData
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

@app.task
def exportUserDataTask():
    users = getUserData()
    exportCSV(users)

def getUserData():
  users = get_user_model().objects.all().order_by('date_joined')
  categories = Category.objects.all().order_by('created_at')
  result = []
  for user in users:
    temp_user = {}
    temp_user['id'] = user.id
    temp_user['username'] = user.username
    temp_user['email'] = user.email
    temp_user['is_superuser'] = user.is_superuser
    if user.last_login is not None:
      temp_user['last_login'] = user.last_login.strftime("%d-%m-%Y %H:%M:%S")
    if user.date_joined is not None:
      temp_user['date_joined'] = user.date_joined.strftime("%d-%m-%Y %H:%M:%S")
    
    for category in categories:
      temp_user[str(category.name)] = category.get_total_score_of_user(user.id)
    result.append(temp_user)
  return result

def exportCSV(users):
  categories = Category.objects.all().order_by('created_at')
  category_names = []
  for category in categories:
    category_names.append(category.name)
  with open('export/user_data.csv', 'w') as csvfile:
    headers = ['id', 'username', 'email', 'date_joined', 'last_login', 'is_superuser'] + category_names
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for user in users:
      writer.writerow(user)

  file_name = 'user_data.csv'
  with open('export/user_data.csv', 'rb') as f:
    content = f.read()
  compress_content = zlib.compress(content)
  file = UserData.objects.filter(file_name=file_name)
  if len(file) == 0:
    user_data = UserData.objects.create(file_name=file_name, content=compress_content)
    user_data.save()
  else:
    user_data=file[0]
    user_data.content=compress_content
    user_data.save()

