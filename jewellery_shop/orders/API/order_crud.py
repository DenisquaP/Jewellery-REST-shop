from rest_framework import viewsets

from orders.models import Order
from orders.serializers.order_serializer import OrderSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
