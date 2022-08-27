from django.urls import path
from .views import *

urlpatterns = [
    path('', HiringApiView.as_view()),  
    path('<int:pk>/', HiringDetailApiView.as_view()),
    path('create/', HiringCreateApiView.as_view()),
    path('<int:pk>/delete/', HiringDeleteApiView.as_view()),
    path('<int:pk>/update/', HiringUpdateApiView.as_view()),
    path('tags/', TagsApiView.as_view()),  
    path('tags/<int:pk>/', TagsDetailApiView.as_view()),
    path('tags/create/', TagsCreateApiView.as_view()),
]
