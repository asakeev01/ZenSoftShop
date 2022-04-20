from rest_framework.response import Response
from rest_framework import viewsets

from .filters import *
from .serializers import *
from .models import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ProductSearchFilter]
    search_fields = ['name', 'categories__title']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductDetailSerializer(instance, context={'request':request})
        return Response(serializer.data)
