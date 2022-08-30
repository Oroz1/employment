from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView, 
    CreateAPIView,
)
from django.db.models import Q
from hiring.models import Hiring, Tags
from rest_framework.permissions import AllowAny, IsAuthenticated

from summary.models import Occupations
from .serializers import HiringViewSerializer, HiringSerializer, TagsSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerPermission
from django_filters import rest_framework as filters
from .filter import HiringFilter

class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class HiringApiView(ListAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringViewSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'company',
        'tags',
        'min_salary',
        'max_salary',
        'currency',
    )
    
    def get_queryset(self):
        request = self.request
        count = request.GET.get('count', None)
        occupation = request.GET.get('occupation', None)
        if count is not None:
            self.queryset = self.queryset[:int(count)]
        if occupation is not None:
            occupation = Occupations.objects.get(id=int(occupation))
            self.queryset = self.queryset.filter(
                Q(occupation__in=occupation.attributes.all()) | Q(occupation=occupation))
        return self.queryset


class HiringDetailApiView(RetrieveAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringViewSerializer
    permission_classes = (AllowAny,)


class HiringCreateApiView(CreateAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated,)


class HiringDeleteApiView(RetrieveDestroyAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)


class HiringUpdateApiView(RetrieveUpdateAPIView):
    queryset = Hiring.objects.all()
    serializer_class = HiringSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,) 
    


class TagsApiView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)


class TagsDetailApiView(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)


class TagsCreateApiView(CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (IsAuthenticated,)