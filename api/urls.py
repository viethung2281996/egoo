from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token
from units.views import ListUnitInCategory, ListUnit, DetailUnit
from conversations.views import ListConversationInUnit, ListConversation, DetailConversation
from categories.views import ListCategory, ListCategory

urlpatterns = [
    #authenticate url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),

    #app url
    path('categories/', ListCategory.as_view()),
    path('categories/<int:pk>/', ListCategory.as_view()),

    path('units/', ListUnit.as_view()),
    path('units/<int:pk>/', DetailUnit.as_view()),
    path('categories/<int:category_id>/units/', ListUnitInCategory.as_view()),

    path('conversations/', ListConversation.as_view()),
    path('conversations/', DetailConversation.as_view()),
    path('categories/<int:category_id>/units/<int:unit_id>/conversations/', ListConversationInUnit.as_view()),
]