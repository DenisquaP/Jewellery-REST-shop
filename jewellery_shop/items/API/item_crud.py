from rest_framework import viewsets
from items.serializers.item_serializer import ItemSerializer
from items.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
