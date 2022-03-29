from xml.dom import ValidationErr
from django.db import models

from ckeditor.fields import RichTextField
from django.forms import ValidationError

from apps.categories.models import *


class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = RichTextField()
    categories = models.ManyToManyField(Category, blank = True)
    vendor_code = models.CharField(max_length = 10, unique = True)
    price = models.DecimalField(max_digits = 20, decimal_places = 2)
    old_price = models.DecimalField(max_digits = 20, decimal_places = 2, blank = True, null = True)
    compound = models.CharField(max_length = 255, blank = True, null = True)
    material = models.CharField(max_length = 255, blank = True, null = True)
    new = models.BooleanField(default = True)
    bestseller = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def clean(self):
        if len(Color.objects.all()) >= 8:
            raise ValidationError("No more than 8 colors")


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_items")
    color = models.ForeignKey(Color, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.color} {self.product.name}"

    def clean(self):
        product_items = ProductItem.objects.filter(product = self.product)
        for i in product_items:
            if self.color == i.color:
                raise ValidationError(f"Only one {self.color} {self.product.name}")
            


class Size(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete = models.CASCADE)
    number = models.CharField(max_length = 100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number} size {self.productItem.color} of {self.productItem.product.name}"


class ProductItemImage(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete = models.CASCADE, related_name = "product_item_images")
    image = models.ImageField(upload_to = 'productItemImage')

    def clean(self):
        if len(ProductItemImage.objects.filter(productItem = self.productItem)) >= 8:
            raise ValidationError("No more than 8 images per item")

    def __str__(self):
        return f"image of {self.productItem.color} {self.productItem.product.name}"
    



    


        