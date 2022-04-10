from rest_framework.views import APIView
from rest_framework.response import Response

from .paginators import *
from .serializers import *
from .models import *

from apps.categories.models import *
from apps.products.models import Product

from apps.products.serializers import ProductSerializer
from apps.categories.serializers import CategoryListSerializer


class MainListView(APIView):
    def get(self, request):
        paginator_items = MainPageItemsPagination()
        paginator_main = MainPagePagination()
        slider = Slider.objects.first()
        slider_ser = SliderSerializer(slider, context={'request': request})
        bestsellers = Product.objects.filter(bestseller=True)
        bestseller_page = paginator_main.paginate_queryset(bestsellers, request)
        bestseller_ser = ProductSerializer(bestseller_page, many=True)
        new = Product.objects.filter(new=True)
        new_page = paginator_items.paginate_queryset(new, request)
        new_ser = ProductSerializer(new_page, many=True)
        categories = Category.objects.all()
        category_page = paginator_items.paginate_queryset(categories, request)
        category_ser = CategoryListSerializer(category_page, many=True)
        advantages = Advantage.objects.all()
        advantage_page = paginator_items.paginate_queryset(advantages, request)
        advantage_ser = AdvantageSerializer(advantage_page, many=True)
        response_data = {
            'slider':slider_ser.data,
            'bestsellers':bestseller_ser.data,
            'new products':new_ser.data,
            'categories':category_ser.data,
            'advantages':advantage_ser.data
        }
        return paginator_main.get_paginated_response(response_data)