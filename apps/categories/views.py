from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.paginator import Paginator

from .paginators import *
from .models import *
from .serializers import *


class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.all().order_by('id')
        paginator = CategoryListPaginator()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CategoryListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


    # paginator_class = CategoryListPaginator
    # serializer_class = CategoryListSerializer
    #
    # @property
    # def paginator(self):
    #     """The paginator instance associated with the view, or `None`."""
    #     if not hasattr(self, '_paginator'):
    #         if self.paginator_class is None:
    #             self._paginator = None
    #         else:
    #             self._paginator = self.paginator_class()
    #     return self._paginator
    #
    # def paginate_queryset(self, queryset):
    #     """Return a single page of results, or `None` if pagination is disabled."""
    #     if self.paginator is None:
    #         return None
    #     return self.paginator.paginate_queryset(queryset, self.request, view=self)
    #
    # def get_paginated_response(self, data):
    #     """Return a paginated style `Response` object for the given output data."""
    #     assert self.paginator is not None
    #     return self.paginator.get_paginated_response(data)
    #
    # def get(self, request):
    #     queryset = Category.objects.all().order_by('id')
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.serializer_class(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

