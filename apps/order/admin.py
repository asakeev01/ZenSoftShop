from django.contrib import admin

from .models import *


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('basket', 'user')


admin.site.register(Order, OrderAdmin)
