from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('login/', obtain_auth_token),
    path('user/', CurrentUser.as_view()),
    path('registration/', RegistrationAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]