from django.db import models

from django.contrib.auth.models import User

from apps.basket.models import *


STATUS = (
    ('New', 'New'),
    ('Paid', 'Paid'),
    ('Canceled', 'Canceled')
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='order')
    number = models.CharField(max_length=20)
    country = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=55)