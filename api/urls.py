from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from user.views import CreateUserView
from rest_framework_jwt.views import refresh_jwt_token
from units.views import ListUnit, DetailUnit, UnitUploadImage, ListUnitInCategory
from conversations.views import ListConversation, DetailConversation, UploadImage, ConversationUploadAudio, ListConversationInUnit
from categories.views import ListCategory, DetaiCategory, CategoryUploadImage, UserGetTotalScore, CategoryActivationCode, AdminGenerateCode
from notes.views import ListNote, DetailNote, UploadAudio, ListNoteInUnit
from speakers.views import ListSpeaker, DetailSpeaker
from user.views import ListUser, DetailUser, UserUploadAvatar, UserActiveCodeView, UserTicketsView, AdminActiveCodeView, AdminGetTotalScore, AdminGetTotalScoreUnit, ExportDataUserView
from guides.views import ListGuide, DetailGuide, GuideOfUnit, GuideUploadImage, GuideUploadVideo
from exsercises.views import ListListenAndReadExsercise, DetailListenAndReadExsercise, ListenAndReadExserciseUploadImage, \
ListenAndReadExserciseUploadAudio, ListChoseAnswerExsercise, DetailChoseAnswerExsercise, ListRewriteSentenceExsercise, \
DetailRewriteSentenceExsercise, ListTranslateSentenceExsercise, DetailTranslateSentenceExsercise, ChoseAnswerExserciseUploadImage, \
ChoseAnswerExserciseUploadAudio, TranslateSentenceExserciseUploadImage, RewriteSentenceExserciseUploadAudio, ExsercisesOfUnit, \
ListExsercise, DetailExsercise
from readings.views import ListReading, DetailReading, ReadingOfUnit, ListQuestion, DetailQuestion

urlpatterns = [
    #authenticate url
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', CreateUserView.as_view(), name='user_register'),
    path('refresh-token/', refresh_jwt_token),

    #app url
    path('categories/', ListCategory.as_view()),
    path('categories/<uuid:pk>/', DetaiCategory.as_view()),
    path('categories/<uuid:category_id>/image', CategoryUploadImage.as_view()),
    path('categories/total_score/', UserGetTotalScore.as_view()),
    path('categories/<uuid:category_id>/codes', CategoryActivationCode.as_view()),
    path('categories/<uuid:category_id>/generate_code', AdminGenerateCode.as_view()),

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

    path('speakers/', ListSpeaker.as_view()),
    path('speakers/<int:pk>/', DetailSpeaker.as_view()),

    path('guides/', ListGuide.as_view()),
    path('guides/<uuid:pk>/', DetailGuide.as_view()),
    path('categories/<uuid:category_id>/units/<uuid:unit_id>/guide/', GuideOfUnit.as_view()),
    path('guides/<uuid:guide_id>/image', GuideUploadImage.as_view()),
    path('guides/<uuid:guide_id>/video', GuideUploadVideo.as_view()),

    path('users/', ListUser.as_view()),
    path('users/<int:pk>/', DetailUser.as_view()),
    path('users/<int:pk>/avatar', UserUploadAvatar.as_view()),
    path('users/<int:pk>/tickets', UserTicketsView.as_view()),
    path('users/code', UserActiveCodeView.as_view()),
    path('users/<int:pk>/admin_active_code', AdminActiveCodeView.as_view()),
    path('users/<int:pk>/scores', AdminGetTotalScore.as_view()),
    path('users/<int:pk>/unit-score', AdminGetTotalScoreUnit.as_view()),
    path('users/export-data-users', ExportDataUserView.as_view()),

    path('exsercises/<uuid:pk>/', DetailExsercise.as_view()),

    path('exsercises/listen_and_read/', ListListenAndReadExsercise.as_view()),
    path('exsercises/listen_and_read/<uuid:pk>/', DetailListenAndReadExsercise.as_view()),
    path('exsercises/listen_and_read/<uuid:exsercise_id>/image', ListenAndReadExserciseUploadImage.as_view()),
    path('exsercises/listen_and_read/<uuid:exsercise_id>/audio', ListenAndReadExserciseUploadAudio.as_view()),

    path('exsercises/chose_answer/', ListChoseAnswerExsercise.as_view()),
    path('exsercises/chose_answer/<uuid:pk>/', DetailChoseAnswerExsercise.as_view()),
    path('exsercises/chose_answer/<uuid:exsercise_id>/image', ChoseAnswerExserciseUploadImage.as_view()),
    path('exsercises/chose_answer/<uuid:exsercise_id>/audio', ChoseAnswerExserciseUploadAudio.as_view()),

    path('exsercises/rewrite_answer/', ListRewriteSentenceExsercise.as_view()),
    path('exsercises/rewrite_answer/<uuid:pk>/', DetailRewriteSentenceExsercise.as_view()),
    path('exsercises/rewrite_answer/<uuid:exsercise_id>/audio', RewriteSentenceExserciseUploadAudio.as_view()),

    path('exsercises/translate/', ListTranslateSentenceExsercise.as_view()),
    path('exsercises/translate/<uuid:pk>/', DetailTranslateSentenceExsercise.as_view()),
    path('exsercises/translate/<uuid:exsercise_id>/image', TranslateSentenceExserciseUploadImage.as_view()),

    path('categories/<uuid:category_id>/units/<uuid:unit_id>/exsercises/', ExsercisesOfUnit.as_view()),

    path('readings/', ListReading.as_view()),
    path('readings/<uuid:pk>/', DetailReading.as_view()),
    path('categories/<uuid:category_id>/units/<uuid:unit_id>/reading/', ReadingOfUnit.as_view()),

    path('questions/', ListQuestion.as_view()),
    path('questions/<uuid:pk>/', DetailQuestion.as_view()),
]