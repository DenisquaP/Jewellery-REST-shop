from rest_framework.viewsets import ModelViewSet
from customers.models import Customer
from customers.serializers.customer_serializer import CustomerSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
