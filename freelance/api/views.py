from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView, 
    CreateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import OrdersDetailSerializer, OrdersListSerializer, OrdersSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerPermission
from freelance.models import Orders


class PaginationApi(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class OrdersApiView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersListSerializer
    permission_classes = (AllowAny,)
    pagination_class  = PaginationApi


class OrdersDetailApiView(RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersDetailSerializer
    permission_classes = (AllowAny,)


class OrdersCreateApiView(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated,)


class OrdersDeleteApiView(RetrieveDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)


class OrdersUpdateApiView(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission,)