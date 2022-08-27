from dataclasses import fields
from rest_framework import serializers
from hiring.models import Hiring, Tags
from summary.models import Summaries
from summary.api.serializers import OccupationsViewSerializer
from company.api.serializers import CompaniesViewSerializer



class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


class SummariesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Summaries
        fields = (
            'id',
            'first_name',
            'surname'
        )


class HiringViewSerializer(serializers.ModelSerializer):

    tags = TagsSerializer(many=True)
    responses = SummariesSerializer(many=True)
    company = CompaniesViewSerializer()
    occupation = OccupationsViewSerializer()

    class Meta:
        model = Hiring
        fields = '__all__'


class HiringSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Hiring
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = '__all__'