from rest_framework.views import APIView
from commons.permissions import UserPermission, AdminPermission

class UserAPIView(APIView):
  permission_classes = (UserPermission,)

class AdminAPIView(APIView):
  permission_classes = (AdminPermission,)