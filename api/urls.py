from django.shortcuts import render

# Create your views here.
from django.urls import path, include


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]