from rest_framework import viewsets
from items.serializers.serializer import ItemSerializer
from items.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
