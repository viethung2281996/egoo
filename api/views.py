from rest_framework.views import APIView
from api.permissons import UserPermission

class BaseAPIView(APIView):
  permission_classes = (UserPermission,)