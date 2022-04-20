from django.contrib import admin

from .models import *

from apps.order.models import Order


class BasketItemInline(admin.StackedInline):
    readonly_fields = ('product_item', 'size')
    model = BasketItem

class BasketAdmin(admin.ModelAdmin):
    inlines = [BasketItemInline,]


admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem)
