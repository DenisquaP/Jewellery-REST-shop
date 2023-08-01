from django.urls import path, include
from rest_framework import routers
from items.API.item_crud import ItemViewSet

router = routers.SimpleRouter()
router.register(r'item', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
