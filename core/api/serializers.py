from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from core.models import *


class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Users
        fields = (
            'avatar',
            'username',
            'first_name', 
            'last_name',
            'email',
            'phone_number',
            'gender',
            'date_of_birth',
            'password',
        )
        

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'avatar',
            'username',
            'first_name', 
            'last_name',
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