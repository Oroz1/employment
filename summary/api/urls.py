from django.urls import path
from .views import *

urlpatterns = [
    path('occupations/', OccupationsApiView.as_view()),  
    path('occupations/<int:pk>/', OccupationsDetailApiView.as_view()),
]
