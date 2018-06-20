from django.db import models
from categories.models import Category
#Create your models here.

class Unit(models.Model):
  title = models.CharField(null=False, max_length=100)
  order = models.IntegerField(null=False)
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    )

  def __str__(self):
    return "Unit: %s" % self.title