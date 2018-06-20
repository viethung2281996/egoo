# units/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ListConversation.as_view()),
    path('<int:pk>/', views.DetailConversation.as_view()),
    # url(r'^', views.conversation_list),
]