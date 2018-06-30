from django.db import models
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='categories/images/', null=True, storage=OverwriteStorage())

  def __str__(self):
    return "Category: %s" % self.name