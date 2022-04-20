from django.contrib import admin

from .models import *
from .forms import *


class ProductItemAdmin(admin.ModelAdmin):
    form = ProductItemForm


admin.site.register(Product)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(ProductItemImage)
admin.site.register(Size)
admin.site.register(Color)
