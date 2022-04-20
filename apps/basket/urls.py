# from django.urls import path
#
# from . import views
#
# from apps.products.views import ProductDetailView
#
#
# urlpatterns = [
#     path('', views.BasketItemCreateView.as_view(), name="basket"),
# ]

from .views import BasketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BasketViewSet, basename='basket')
urlpatterns = router.urls