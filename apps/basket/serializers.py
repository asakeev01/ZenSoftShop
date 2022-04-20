from rest_framework import serializers

from apps.products.serializers import ProductItemSerializer

from .models import *


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('user', 'sum', 'discount_sum', 'price_sum')


class BasketItemSerializer(serializers.ModelSerializer):
    basket = BasketSerializer()
    product_item = ProductItemSerializer()

    class Meta:
        model = BasketItem
        fields = ('basket', 'product_item', 'size', 'quantity', 'items_price', 'items_discount')


class BasketItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ('product_item', 'size', 'quantity')

    def create(self, validated_data):
        size = self.validated_data['size']
        quantity = self.validated_data['quantity']
        if quantity > size.quantity:
            raise serializers.ValidationError("not enough quantity")
        else:
            request = self.context.get("request")
            user = request.user
            basket = Basket.objects.get(user=user)
            basket_item = BasketItem.objects.create(basket=basket, **validated_data)
            return basket_item


