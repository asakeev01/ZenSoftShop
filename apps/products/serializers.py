from rest_framework import serializers

from .models import *


class ProductItemImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItemImage
        fields = ('image', 'productItem')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('number', 'quantity')


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('name',)


class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    colors = ColorSerializer(many=True)
    product_item_images = ProductItemImageSerializer(many=True)
    sizes = SizeSerializer(many=True)

    class Meta:
        model = ProductItem
        fields = ('id', 'colors', 'product_item_images', 'sizes')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'description', 'categories', 'vendor_code', 'price', 'old_price', 'compound', 'material', 'new', 'bestseller')


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItemSerializer(many = True)

    class Meta:
        model = Product
        fields = ('url', 'name', 'description', 'categories', 'vendor_code', 'price', 'old_price', 'compound', 'material', 'new', 'bestseller', 'product_items')








