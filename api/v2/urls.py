from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token
from categories.api.v2.views import ListCategory

urlpatterns = [
    path('categories/', ListCategory.as_view()),
]