from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
<<<<<<< HEAD
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('categories/', include('categories.urls')),
=======
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),
>>>>>>> e4698b36abc676477a338c4c7634f1e504e65d66
]