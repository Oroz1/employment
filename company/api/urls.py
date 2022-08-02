from django.urls import path

from .views import *


urlpatterns = [
    
    path('', CompaniesApiView.as_view()),  
    path('<int:pk>/', CompaniesDetailApiView.as_view()),
    path('create/', CompaniesCreateApiView.as_view()),
    path('<int:pk>/delete/', CompaniesDeleteApiView.as_view()),
    path('<int:pk>/update/', CompaniesUpdateApiView.as_view()),
  
]