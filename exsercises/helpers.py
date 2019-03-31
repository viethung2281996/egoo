from commons.common_helpers import CommonHelper
from .models import Exsercise, ListenAndReadExsercise, ChoseAnswerExsercise
from .serializers import ExserciseSerializer, ListenAndReadExserciseSerializer, ChoseAnswerExserciseSerializer

class ExserciseHelper(CommonHelper):
  model_class = Exsercise
  serializer_class = ListenAndReadExserciseSerializer

class ListenAndReadExserciseHelper(ExserciseHelper):
  model_class = ListenAndReadExsercise
  serializer_class = ListenAndReadExserciseSerializer

class ChoseAnswerExserciseHelper(ExserciseHelper):
  model_class = ChoseAnswerExsercise
  serializer_class = ChoseAnswerExserciseSerializer
