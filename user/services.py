from categories.models import ActivationCode
from django.contrib.auth import get_user_model
from user.models import Ticket
from django.core.exceptions import ObjectDoesNotExist
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
      if activation_code.status == UserActivedCode.CODE_USED:
        self.messages.append('Code are used')
        raise Exception()
      else:
        return activation_code
    except ObjectDoesNotExist as e:
      self.messages.append('Code are not available')
      raise e
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
    start_time = datetime.datetime.now()
    end_time = None
    if activation_code.time is not None:
      end_time = start_time + activation_code.time
    ticket = Ticket(user=user,
                    activation_code=activation_code,
                    category=activation_code.category, 
                    start=start_time,
                    end=end_time)
    ticket.save()
    activation_code.status = UserActivedCode.CODE_USED
    activation_code.save()