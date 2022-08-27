from dataclasses import fields
from rest_framework import serializers
from freelance.models import Orders
from hiring.api.serializers import TagsSerializer
from summary.models import Summaries


class OrdersListSerializer(serializers.ModelSerializer):

    tags = TagsSerializer()
    owner = serializers.ReadOnlyField(source='get_full_name')

    class Meta:
        model = Orders
        exclude = ('responses', 'maker')
        
        
class OrdersSummariesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Summaries
        fields = (
            'id',
            'first_name',
            'surname',
            'phone_number',
        )        
        
        
class OrdersDetailSerializer(serializers.ModelSerializer):
    
    tags = TagsSerializer()
    responses = OrdersSummariesSerializer()

    class Meta:
        model = Orders
        fields = '__all__'
        

class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'




