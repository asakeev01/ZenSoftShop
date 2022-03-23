from email.quoprimime import unquote
from unicodedata import decimal
from django.db import models

from ckeditor.fields import RichTextField


PRODUCT_ITEM_COLORS = (
    ('BLACK', 'Black'),
    ('RED', 'Red'),
    ('ORANGE', 'Orange'),
    ('BROWN', 'Brown'),
    ('PURPLE', 'Purple'),
    ('YELLOW', 'Yellow'),
    ('BLUE', 'Blue'),
    )


class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = RichTextField()

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    vendor_code = models.CharField(max_length = 10, unique = True)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)
    old_price = models.DecimalField(max_digits = 20, decimal_places = 2, blank = True)
    color = models.CharField(max_length = 50, choices = PRODUCT_ITEM_COLORS, unique = True)

    def __str__(self):
        return f"{self.color} of {self.product.name}"


class Size(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete = models.CASCADE)
    number = models.CharField(max_length = 100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number} size {self.productItem.color} of {self.productItem.product.name}"


class ProductItemImage(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete = models.CASCADE)
    image = models.ImageField()

