from rest_framework import generics
from speakers.models import Speaker
from speakers.serializers import SpeakerSerializer
# Create your views here.

class ListSpeaker(generics.ListCreateAPIView):
  queryset = Speaker.objects.all()
  serializer_class = SpeakerSerializer

  def get_queryset(self):
    queryset = Speaker.objects.all()
    user = self.request.query_params.get('user', None)
    unit = self.request.query_params.get('unit', None)
    
    if user is not None and unit is not None:
      return queryset.filter(user=user, unit=unit)
    elif user is not None:
      return queryset.filter(user=user)
    elif unit is not None:
      return queryset.filter(unit=unit)
    else:
      return queryset

class DetailSpeaker(generics.RetrieveUpdateDestroyAPIView):
  queryset = Speaker.objects.all()
  serializer_class = SpeakerSerializer
