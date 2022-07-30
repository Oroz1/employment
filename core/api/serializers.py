from rest_framework import serializers
from core.models import *


class CreateUserProfileSerializer(serializers.ModelSerializer):
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