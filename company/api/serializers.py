from dataclasses import field
from rest_framework import serializers
from company.models import Companies
from core.api.serializers import UserProfileSerializer

class CompaniesViewSerializer(serializers.ModelSerializer):
    
    owner = UserProfileSerializer()

    class Meta:
        model = Companies
        fields = '__all__'


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = '__all__'