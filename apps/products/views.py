from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products import serializers

from apps.products.serializers import ProductDetailSerializer, ProductItemSerializer, ProductSerializer
from apps.products.models import *


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk = pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

class ProductItemListView(APIView):
    def get(self, request, pk):
        product_items = ProductItem.objects.filter(product = pk)
        serializer = ProductItemSerializer(product_items, many = True)
        return Response(serializer.data)


