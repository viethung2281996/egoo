from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    #authenticate url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),

    #app url
    path('categories/', include('categories.urls')),
    path('units/', include('units.urls')),
    path('conversations/', include('conversations.urls')),
]