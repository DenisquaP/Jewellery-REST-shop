from django.db import models
from customers.models import Customer
from items.apps import ItemsConfig


# Create your models here.
class Order(models.Model):
    order_date = models.DateField(verbose_name='order_date', blank=False)
    price = models.PositiveIntegerField(verbose_name='price', blank=False)
    is_ready = models.BooleanField(verbose_name='is_ready', blank=False)

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=False
        )
    items = models.ForeignKey(
        ItemsConfig, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.is_ready)

    class Meta:
        db_table = 'orders'
