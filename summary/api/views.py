from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from hiring.models import Occupations
from rest_framework.permissions import AllowAny
from .serializers import OccupationsViewSerializer
from rest_framework.pagination import PageNumberPagination


class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class OccupationsApiView(ListAPIView):
    queryset = Occupations.objects.all()
    serializer_class = OccupationsViewSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi
    
    def get_queryset(self):
        request = self.request
        is_main = bool(request.GET.get('is_main', None))
        if is_main is not None and is_main:
            self.queryset = Occupations.objects.filter(is_main=True)
        return self.queryset


class OccupationsDetailApiView(RetrieveAPIView):
    queryset = Occupations.objects.all()
    serializer_class = OccupationsViewSerializer
    permission_classes = (AllowAny,)