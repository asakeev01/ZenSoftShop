from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'categories', 'vendor_code', 'price', 'old_price', 'compound', 'material', 'new', 'bestseller')


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'categories', 'vendor_code', 'price', 'old_price', 'compound', 'material', 'new', 'bestseller', 'product_items')


class ProductItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItem
        fields = ('id', 'product', 'color', 'product_item_images')


class ProductItemImage(serializers.ModelSerializer):

    class Meta:
        model = ProductItemImage
        fields = ('image', 'productItem')
