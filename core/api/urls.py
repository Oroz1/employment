from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from .views import *


urlpatterns = [
    path('swagger/', get_swagger_view(title='Cars API')),
    path('login/', obtain_auth_token),
    path('registration/', RegistrationAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]