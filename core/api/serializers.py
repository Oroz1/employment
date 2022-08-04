from rest_framework import serializers
from core.models import *


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'avatar',
            'username',
            'name',
            'email',
            'phone_number',
            'gender',
            'date_of_birth',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'avatar',
            'username',
            'name',
            'email',
            'phone_number',
            'gender',
            'date_of_birth',
        )

        def get_image_url(self, obj):
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image.url)


class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=50,)
    password = serializers.CharField(max_length=50)