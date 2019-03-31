from rest_framework import generics, status
from rest_framework.response import Response
from commons.permissions import UserPermission
from commons.views import UserAPIView, AdminAPIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from categories.models import Category, ActivationCode
from user.models import Ticket
from django.utils import timezone
from categories.serializers import CategorySerializer, ActivationCodeSerializer
from egoo_core.cloudinary import CloudinaryUploader
from categories.services import ActivationCodeGenerator
import datetime
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = (UserPermission,)

  def get_queryset(self):
    return Category.objects.order_by('order')

  def get(self, request):
    serializer = CategorySerializer(Category.objects.all(), many=True)
    categories = serializer.data
    len_categories = len(categories)
    if request.user.is_superuser:
      for i in range(0, len_categories):
        categories[i]['has_permission'] = True  
    else:
      for i in range(0, len_categories):
        if categories[i]['type'] == 'Free':
          categories[i]['has_permission'] = True
        else:
          ticket = Ticket.objects.filter(user=request.user, category__id=categories[i]['id'], status='Active').first()
          if ticket is not None:
            if ticket.end is None or ticket.end > datetime.datetime.now(tz=timezone.utc):
              categories[i]['has_permission'] = True
            else:
              ticket.status = 'Expired'
              ticket.save()
              categories[i]['has_permission'] = False
          else:
            categories[i]['has_permission'] = False
    return Response(categories)

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = (UserPermission,)

@parser_classes((MultiPartParser, ))
class CategoryUploadImage(AdminAPIView):
  def post(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)

    data = {}
    file = request.data['image']
    file_name = category.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)

    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="categories/images")
    r = uploader.upload()

    data['image'] = r['secure_url']
    serializer = CategorySerializer(category, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)

class UserGetTotalScore(UserAPIView):
  def get(self, request):
    user_id = self.request.user.id

    categories = Category.objects.all()
    category_score = []

    for category in categories:
      data = {}
      data['id'] = str(category.id)
      data['name'] = category.name
      data['total_score'] = category.get_total_score_of_user(user_id)

      category_score.append(data)

    return Response(category_score)

class CategoryActivationCode(AdminAPIView):
  def get(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
      
    activation_codes = category.activation_codes
    serializer = ActivationCodeSerializer(activation_codes, many=True)
    return Response(serializer.data)

class AdminGenerateCode(AdminAPIView):
  def post(self, request, category_id):
    data = request.data
    quantity = data['quantity']
    time = data['time']
    type = data['type']
    generator = ActivationCodeGenerator(category_id, quantity, time, type)
    result = generator.generate_actication_code()
    if result:
      return Response(status=status.HTTP_200_OK)
    else:
      return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)