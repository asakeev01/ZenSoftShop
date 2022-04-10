from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse

from apps.products.models import *
from apps.products.serializers import *

from .paginators import *
from .models import *
from .serializers import *


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all().order_by('id')
        paginator = CategoryListPaginator()
        page = paginator.paginate_queryset(categories, request)
        serializer = CategoryListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(categories__id=category.id)
        products_new = Product.objects.filter(categories__id=category.id, new=True)
        paginator = CategoryDetailPaginator()
        paginator_new = CategoryDetailNewPaginator()
        page = paginator.paginate_queryset(products, request)
        page_new = paginator_new.paginate_queryset(products_new, request)
        serializer = ProductSerializer(page, many=True, context={'request':request})
        serializer_new = ProductSerializer(page_new, many=True, context={'request':request})
        response_data = {
            "products":serializer.data,
            "products_new":serializer_new.data
        }
        return paginator.get_paginated_response(response_data)


