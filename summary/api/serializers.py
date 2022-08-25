from dataclasses import field
from rest_framework import serializers
from summary.models import Summaries, Occupations


class OccupationsAttributesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occupations
        fields = '__all__'


class OccupationsViewSerializer(serializers.ModelSerializer):

    attributes = OccupationsAttributesSerializer(many=True)

    class Meta:
        model = Occupations
        fields = '__all__'

    

class SummariesViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Summaries
        fields = '__all__'


