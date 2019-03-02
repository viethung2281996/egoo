from rest_framework import generics
from rest_framework.response import Response
from api.permissons import UserPermission
from categories.models import Category
from user.models import Ticket
from .serializers import CategorySerializer
from api.views import BaseAPIView
import datetime
# Create your views here.

class ListCategory(BaseAPIView):
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
		        if ticket.end is None or ticket.end < datetime.datetime.now():
		          categories[i]['has_permission'] = True
		        else:
		          ticket.status = 'Expired'
		          ticket.save()
		          categories[i]['has_permission'] = False
		      else:
		        categories[i]['has_permission'] = False
		return Response(categories)

