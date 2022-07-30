from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import *
from .serializers import *


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserProfileSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        password = make_password(self.request.data['password'])
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=password)
        token = Token.objects.get_or_create(user=user)[0].key
        data = {}
        data["message"] = "Пользователь успешно зарегистрирован"
        data["username"] = user.username
        data["token"] = token
        return Response(data, status=200)