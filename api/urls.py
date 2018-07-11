from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token
from units.views import ListUnit, DetailUnit, UnitUploadImage, ListUnitInCategory
from conversations.views import ListConversation, DetailConversation, UploadImage, ConversationUploadAudio, ListConversationInUnit
from categories.views import ListCategory, DetaiCategory, CategoryUploadImage
from notes.views import ListNote, DetailNote, UploadAudio, ListNoteInUnit
from user.views import ListUser, DetailUser

urlpatterns = [
    #authenticate url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),

    #app url
    path('categories/', ListCategory.as_view()),
    path('categories/<uuid:pk>/', DetaiCategory.as_view()),
    path('categories/<uuid:category_id>/image', CategoryUploadImage.as_view()),

    path('units/', ListUnit.as_view()),
    path('units/<uuid:pk>/', DetailUnit.as_view()),
    path('units/<uuid:unit_id>/image', UnitUploadImage.as_view()),
    path('categories/<uuid:category_id>/units/', ListUnitInCategory.as_view()),

    path('conversations/', ListConversation.as_view()),
    path('conversations/<uuid:pk>/', DetailConversation.as_view()),
    path('categories/<uuid:category_id>/units/<uuid:unit_id>/conversations/', ListConversationInUnit.as_view()),
    path('conversations/<uuid:conversation_id>/image', UploadImage.as_view()),
    path('conversations/<uuid:conversation_id>/audio', ConversationUploadAudio.as_view()),

    path('notes/', ListNote.as_view()),
    path('notes/<uuid:pk>/', DetailNote.as_view()),
    path('notes/<uuid:note_id>/audio', UploadAudio.as_view()),
    path('categories/<uuid:category_id>/units/<uuid:unit_id>/notes/', ListNoteInUnit.as_view()),

    path('users/', ListUser.as_view()),
    path('users/<int:pk>/', DetailUser.as_view()),
]