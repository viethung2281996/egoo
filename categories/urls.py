# units/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ListCategory.as_view()),
    path('<int:pk>/', views.DetaiCategory.as_view()),
    path('<int:pk>/units/', include('units.urls')),
]