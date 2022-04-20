from ckeditor.fields import RichTextField

from django.forms import ValidationError

from apps.categories.models import *

from colorfield.fields import ColorField


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    categories = models.ManyToManyField(Category, blank=True, related_name='products')
    vendor_code = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    old_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    compound = models.CharField(max_length=255, blank = True, null = True)
    material = models.CharField(max_length=255, blank=True, null = True)
    new = models.BooleanField(default=True)
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        if self.old_price == None:
            self.old_price = 0

    @property
    def discount(self):
        if self.old_price != None:
            return self.old_price - self.price
        else:
            return 0


class Color(models.Model):
    rgb = ColorField()

    def __str__(self):
        return self.rgb

    def clean(self):
        if len(Color.objects.all()) >= 8:
            raise ValidationError("No more than 8 colors")


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_items")
    colors = models.ManyToManyField(Color, related_name="product_item", blank=False)

    def __str__(self):
        return f"{self.colors} {self.product.name}"

    @property
    def old_price(self):
        return self.product.old_price

    @property
    def price(self):
        return self.product.price

    @property
    def discount(self):
        return self.product.discount


class Size(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete = models.CASCADE, related_name="sizes")
    number = models.CharField(max_length = 100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number} size {self.productItem.colors} of {self.productItem.product.name}"
    
    def clean(self):
        for i in Size.objects.filter(productItem=self.productItem):
            if self.number == i.number:
                raise ValidationError(f"Only one {self.number} size of {self.productItem.colors} {self.productItem.product.name}")


class ProductItemImage(models.Model):
    productItem = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name="product_item_images")
    image = models.ImageField(upload_to='productItemImage')

    def clean(self):
        if len(ProductItemImage.objects.filter(productItem=self.productItem)) >= 8:
            raise ValidationError("No more than 8 images per item")



    
