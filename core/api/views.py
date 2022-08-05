from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import *
from .serializers import *


class RegistrationAPI(GenericAPIView):

    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        password = make_password(self.request.data['password'])
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=password)
        serializer_user = UserProfileSerializer(user, many=False, context={"request": request})
        token = Token.objects.get_or_create(user=user)[0].key
        data = {
            'message': 'Пользователь успешно зарегистрирован',
            'token': token
        }
        profile = serializer_user.data
        data.update(profile)
        return Response(data, status=200)


class CurrentUser(GenericAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, many=False, context={"request": request})
        return Response(serializer.data, status=200)


class LoginApi(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        data = login_serializer.data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            serializer = UserProfileSerializer(user, many=False, context={"request": request})
            token = Token.objects.get_or_create(user=user)[0].key
            data = {'token': f'{token}',}
            profile = serializer.data
            data.update(profile)    
            return Response(data, status=200)
    
        return Response({'detail': 'Не существует пользователя или неверный пароль'})
