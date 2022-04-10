from rest_framework.pagination import PageNumberPagination


class ProductDetailSamePaginator(PageNumberPagination):
    page_size = 5