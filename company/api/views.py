from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView, 
    CreateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CompaniesSerializer, CompaniesViewSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerPermission, isSuperAdminUser
from company.models import Companies


class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class CompaniesApiView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesViewSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi


class CompaniesDetailApiView(RetrieveAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesViewSerializer
    permission_classes = (AllowAny,)


class CompaniesCreateApiView(CreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = (IsAuthenticated,)


class CompaniesDeleteApiView(RetrieveUpdateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission, isSuperAdminUser)


class CompaniesUpdateApiView(RetrieveDestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission, isSuperAdminUser)