from categories.models import ActivationCode
from django.contrib.auth import get_user_model
from user.models import Ticket
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from units.models import Unit
from categories.models import Category
import datetime

class UserActiveCode():
  CODE_USED = 'Used'
  CODE_ACTIVE = 'Active'

  def __init__(self, user_id, code):
    self.user_id = user_id
    self.code = code
    self.messages = []
    self.errors = []
  
  def process(self):
    try:
      activation_code = self.get_activate_code(self.code)
      self.check_user_compatible_with_code(activation_code)
      self.active_code(activation_code)
      return True
    except Exception as e:
      return False

  def get_activate_code(self, code):
    try:
      activation_code = ActivationCode.objects.filter(code=code).first()
      if activation_code is None:
        self.messages.append('Code are not available')
        raise e
      if activation_code.status == UserActiveCode.CODE_USED:
        self.messages.append('Code are used')
        raise Exception()
      else:
        return activation_code
    except Exception as e:
      self.errors.append(repr(e))
      raise e


  def check_user_compatible_with_code(self, activation_code):
    try:
      ticket = Ticket.objects.filter(user__id=self.user_id, category=activation_code.category, status='Active')
      if len(ticket) != 0:
        self.messages.append('User already active category')
        raise Exception()
    except Exception as e:
      self.errors.append(repr(e))
      raise e

  def active_code(self, activation_code):
    user = get_user_model().objects.get(pk=self.user_id)
    start_time = datetime.datetime.now(tz=timezone.utc)
    end_time = None
    if activation_code.time is not None:
      end_time = start_time + activation_code.time
    ticket = Ticket(user=user,
                    activation_code=activation_code,
                    category=activation_code.category, 
                    start=start_time,
                    end=end_time)
    ticket.save()
    activation_code.status = UserActiveCode.CODE_USED
    activation_code.save()

class GetUserScoreUnit():
  def __init__(self, user_id):
    self.user_id = user_id

  def get_scores(self):
    result = []
    units = Unit.objects.all().order_by('category_id')
    categories = Category.objects.all()
    categories_dict = {}
    for category in categories:
      categories_dict[category.id] = category.name
    for unit in units:
        data = {}
        data['category'] = categories_dict[unit.category_id]
        data['unit'] = unit.title
        data['score'] = unit.get_max_score_of_user(self.user_id)
        result.append(data)
    return result