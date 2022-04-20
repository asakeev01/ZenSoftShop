from rest_framework.pagination import PageNumberPagination


class NewsPaginator(PageNumberPagination):
    page_size = 8