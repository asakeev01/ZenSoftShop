from rest_framework.pagination import PageNumberPagination


class CategoryListPaginator(PageNumberPagination):
    page_size = 8


class CategoryDetailPaginator(PageNumberPagination):
    page_size = 12


class CategoryDetailNewPaginator(PageNumberPagination):
    page_size = 5