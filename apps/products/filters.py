from rest_framework.filters import SearchFilter

from .models import Product

from apps.categories.models import Category


class ProductSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        if not super().filter_queryset(request, queryset, view):
            products = []
            for i in Category.objects.all():
                for k in Product.objects.filter(categories=i).order_by('?'):
                    products.append(k.pk)
                    break
                if len(products) == 5:
                    break
            products_queryset = Product.objects.filter(pk__in=products)
            return products_queryset
        return super().filter_queryset(request, queryset, view)
