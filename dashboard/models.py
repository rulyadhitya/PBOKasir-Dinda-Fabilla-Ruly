from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
CATEGORY = (
    ('Fisheries', 'Fisheries'),
    ('Cultivation', 'Cultivation'),
    ('Fishing', 'Fishing'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    product_code = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.product_code}'


class Order(models.Model):
    name = models.ForeignKey(Product,  on_delete=models.CASCADE, null=True)
    product_code = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    timezone.localtime(timezone.now())
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Order'

    def _str_(self):
        return f'{self.customer} ordered by {self.name}'
