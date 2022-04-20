from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoryDetailSerializer(instance)
        return Response(serializer.data)

