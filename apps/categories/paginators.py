from rest_framework.pagination import PageNumberPagination


class CategoryListPaginator(PageNumberPagination):
    page_size = 8