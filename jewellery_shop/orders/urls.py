from django.urls import path, include
from rest_framework import routers

from orders.API.order_crud import OrdersViewSet


router = routers.SimpleRouter()
router.register(r'order', OrdersViewSet)

urlpatterns = [
    path('', include(router.urls))
]
