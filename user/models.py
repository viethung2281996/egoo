import uuid
from django.db import models
from commons.models import BaseModel
from django.contrib.auth.models import User
from categories.models import Category, ActivationCode

STATUS_CHOICE = (
  ('Active', 'Active'),
  ('Expired', 'Expired'),
  ('Blocked', 'Blocked'),
  )

class CustomInformation(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.CharField(max_length=100, blank=True, null=True)

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("user", self.id)

class Ticket(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  status = models.CharField(null=False, max_length=20, choices=STATUS_CHOICE, default='Active')
  user = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
    )
  category = models.ForeignKey(
      Category,
      on_delete=models.CASCADE,
    )
  activation_code = models.OneToOneField(
      ActivationCode,
      on_delete=models.DO_NOTHING,
    )
  start = models.DateTimeField(null=False)
  end = models.DateTimeField(null=True)
  
  class Meta:
    unique_together = ('user', 'category', 'activation_code')

class UserData(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  file_name = models.CharField(max_length=100, blank=False, null=False)
  content = models.BinaryField()