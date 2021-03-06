from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(null=False, max_digits=4, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
    