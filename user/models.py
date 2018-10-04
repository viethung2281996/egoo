from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomInformation(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.CharField(max_length=100, blank=True, null=True)

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("user", self.id)
