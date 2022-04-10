from rest_framework.pagination import PageNumberPagination


class MainPagePagination(PageNumberPagination):
    page_size = 8


class MainPageItemsPagination(PageNumberPagination):
    page_size = 4