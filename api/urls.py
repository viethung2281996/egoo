from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
]