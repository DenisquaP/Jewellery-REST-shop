from django.contrib import admin
from orders.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'is_ready')
    list_filter = ('is_ready', 'price', 'order_date')
