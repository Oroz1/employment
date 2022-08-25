import django_filters
from hiring.models import *


class HiringFilter(django_filters.FilterSet):
    
    class Meta:
        model = Hiring
        fields = '__all__'