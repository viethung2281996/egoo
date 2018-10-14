from rest_framework.views import APIView
from api.permissons import UserPermission, AdminPermission

class BaseAPIView(APIView):
  permission_classes = (UserPermission,)

class AdminAPIView(APIView):
  permission_classes = (AdminPermission,)