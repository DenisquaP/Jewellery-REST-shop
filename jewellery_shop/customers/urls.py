from django.urls import path, include
from rest_framework import routers
from customers.API.customer_crud import CustomerViewSet

router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
