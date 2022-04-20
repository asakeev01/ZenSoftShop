from rest_framework import serializers

from .models import *

from apps.products.serializers import ProductSerializer


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'parent')

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields  = ('id', 'title', 'image', 'parent', 'products')