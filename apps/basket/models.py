from django.db import models
from django.contrib.auth.models import User

from apps.products.models import ProductItem, Size


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def price_sum(self):
        summa = self.sum + self.discount_sum
        return summa

    @property
    def discount_sum(self):
        summa = sum([i.items_discount for i in self.basket_items.all()])
        return summa

    @property
    def sum(self):
        summa = sum([i.items_price for i in self.basket_items.all()])
        return summa


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_items')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def items_price(self):
        return self.product_item.price * self.quantity

    @property
    def items_discount(self):
        return self.product_item.discount * self.quantity
