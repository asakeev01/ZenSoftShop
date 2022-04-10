from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User

from apps.users.models import *


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


class ProductItemSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    product_item_images = ProductItemImageSerializer(many=True)
    sizes = SizeSerializer(many=True)

    class Meta:
        model = ProductItem
        fields = ('colors', 'product_item_images', 'sizes')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItemSerializer(many=True)
    favorite = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'old_price', 'discount', 'product_items', 'favorite')

    def get_favorite(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        try:
            favorite = Favorite.objects.get(user=user)
            products = Product.objects.filter(favorites=favorite)
            for product in products:
                if product == obj:
                    print(product)
                    return True
            return False
        except:
            return False

    def get_discount(self, obj):
        if obj.old_price != None:
            discount = (obj.old_price - obj.price) * 100 / obj.old_price
            return discount
        else:
            return None


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItemSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'categories', 'vendor_code', 'price', 'old_price', 'compound', 'material', 'new', 'bestseller', 'product_items')








