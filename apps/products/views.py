from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True, context = {'request' : request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk = pk)
        serializer = ProductDetailSerializer(product, context = {'request' : request})
        return Response(serializer.data)


class ProductItemListView(APIView):
    def get(self, request, pk):
        product_items = ProductItem.objects.filter(product = pk)
        serializer = ProductItemSerializer(product_items, many = True, context = {'request' : request})
        return Response(serializer.data)


