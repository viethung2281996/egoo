from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token
from units.views import ListUnit, DetailUnit, ListConversationInUnit, ListNoteInUnit, UnitUploadImage
from conversations.views import ListConversation, DetailConversation, UploadImage, ConversationUploadAudio
from categories.views import ListCategory, DetaiCategory, ListUnitInCategory, CategoryUploadImage
from notes.views import ListNote, DetailNote, UploadAudio

urlpatterns = [
    #authenticate url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),

    #app url
    path('categories/', ListCategory.as_view()),
    path('categories/<int:pk>/', DetaiCategory.as_view()),
    path('categories/<int:category_id>/units/', ListUnitInCategory.as_view()),
    path('categories/<int:category_id>/image', CategoryUploadImage.as_view()),

    path('units/', ListUnit.as_view()),
    path('units/<int:pk>/', DetailUnit.as_view()),
    path('categories/<int:category_id>/units/<int:unit_id>/conversations/', ListConversationInUnit.as_view()),
    path('categories/<int:category_id>/units/<int:unit_id>/notes/', ListNoteInUnit.as_view()),
    path('units/<int:unit_id>/image', UnitUploadImage.as_view()),

    path('conversations/', ListConversation.as_view()),
    path('conversations/<int:pk>/', DetailConversation.as_view()),
    path('conversations/<int:conversation_id>/image', UploadImage.as_view()),
    path('conversations/<int:conversation_id>/audio', ConversationUploadAudio.as_view()),

    path('notes/', ListNote.as_view()),
    path('notes/<int:pk>/', DetailNote.as_view()),
    path('notes/<int:note_id>/audio', UploadAudio.as_view()),
]