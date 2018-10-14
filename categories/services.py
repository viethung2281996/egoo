import uuid
import datetime
from categories.models import Category, ActivationCode
from django.db import IntegrityError

class ActivationCodeGenerator():
  def __init__(self, category_id, quantity, time, type=None):
    try:
      category = Category.objects.get(id=category_id)
    except Exception as e:
      raise e

    self.category = category
    self.quantity = int(quantity)
    self.type = type
    self.time = self.time_format(time)

  @staticmethod
  def time_format(time):
    if time == '1.days':
      return datetime.timedelta(days=1)
    elif time == '1.hours':
      return datetime.timedelta(hours=1)
    else:
      return None

  def generate_actication_code(self):
    result = []
    quantity = self.quantity
    for i in range(quantity):
      category = self.category
      time = self.time
      type = self.type
      try:
        code = self.generate_random_code()
        activation_code = ActivationCode(category=category, time=time, code=code, type=type)
        activation_code.save()
      except Exception as e:
        code = self.generate_random_code()
        activation_code = ActivationCode(category=category, time=time, code=code, type=type)
        activation_code.save()
      result.append(activation_code)
    return result
      
  def generate_random_code(self):
    return uuid.uuid4().hex[:6].upper()

