from commons.helpers import CommonHelper
from .models import Exsercise, ListenAndReadExsercise, ChoseAnswerExsercise, RewriteSentenceExsercise, TranslateSentenceExsercise
from .serializers import ExserciseSerializer, ListenAndReadExserciseSerializer, ChoseAnswerExserciseSerializer, TranslateSentenceExserciseSerializer, RewriteSentenceExserciseSerializer

class ExserciseHelper(CommonHelper):
  model_class = Exsercise
  serializer_class = ListenAndReadExserciseSerializer

class ListenAndReadExserciseHelper(ExserciseHelper):
  model_class = ListenAndReadExsercise
  serializer_class = ListenAndReadExserciseSerializer

class ChoseAnswerExserciseHelper(ExserciseHelper):
  model_class = ChoseAnswerExsercise
  serializer_class = ChoseAnswerExserciseSerializer

class TranslateSentenceExserciseHelper(ExserciseHelper):
  model_class = TranslateSentenceExsercise
  serializer_class = TranslateSentenceExserciseSerializer

class RewriteSentenceExserciseHelper(ExserciseHelper):
  model_class = RewriteSentenceExsercise
  serializer_class = RewriteSentenceExserciseSerializer
