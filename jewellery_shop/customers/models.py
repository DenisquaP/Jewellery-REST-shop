from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(verbose_name='name', blank=False)
    surname = models.CharField(verbose_name='surname', blank=False)
    adress = models.CharField(verbose_name='adress', blank=False)
    phone_number = models.CharField(verbose_name='phone_number', blank=False)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    class Meta:
        db_table = 'customers'
