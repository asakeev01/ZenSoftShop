from rest_framework import viewsets

from rest_framework import generics
from rest_framework import viewsets

from django.core.exceptions import ValidationError
from .models import *

from .forms import *
from .serializers import *


class BasketViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        basket = Basket.objects.get(user=self.request.user)
        basket_items = BasketItem.objects.filter(basket=basket)
        return basket_items
    serializer_class = BasketItemSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return BasketItemCreateSerializer
        else:
            return BasketItemSerializer
