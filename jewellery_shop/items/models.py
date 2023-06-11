from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(verbose_name='name', blank=False)
    description = models.CharField(verbose_name='description', blank=False)
    article = models.CharField(verbose_name='article', blank=False)
    weight = models.PositiveIntegerField(verbose_name='weight', blank=False)
    price = models.PositiveIntegerField(verbose_name='price', blank=False)
    material = models.CharField(verbose_name='material', blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'items'
