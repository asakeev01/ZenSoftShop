from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *
from .paginators import *


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk, pk_category):
        product = Product.objects.get(pk=pk)
        products = Product.objects.filter(categories__id=pk_category).exclude(pk=pk)
        paginator = ProductDetailSamePaginator()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductDetailSerializer(product, context={'request':request})
        serializer_products = ProductSerializer(page, many=True)
        response_data = {'product_detail':serializer.data,
                         'same_products':serializer_products.data}
        return Response(response_data)


class ProductItemListView(APIView):
    def get(self, request, pk):
        product_items = ProductItem.objects.filter(product=pk)
        serializer = ProductItemSerializer(product_items, many = True, context={'request':request})
        return Response(serializer.data)


