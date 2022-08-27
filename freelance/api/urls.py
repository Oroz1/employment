from django.urls import path
from .views import *


urlpatterns = [
    
    path('', OrdersApiView.as_view()),  
    path('<int:pk>/', OrdersDetailApiView.as_view()),
    path('create/', OrdersCreateApiView.as_view()),
    path('<int:pk>/delete/', OrdersDeleteApiView.as_view()),
    path('<int:pk>/update/', OrdersUpdateApiView.as_view()),
  
]