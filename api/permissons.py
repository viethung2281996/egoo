from rest_framework import permissions

class UserPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method == 'GET':
      return request.user.is_authenticated
    else:
      return request.user.is_superuser

class AdminPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.is_superuser