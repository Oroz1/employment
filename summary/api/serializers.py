from rest_framework import serializers
from summary.models import Summaries, Occupations

class OccupationsViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Occupations
        fields = '__all__'

    

class SummariesViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Summaries
        fields = '__all__'


