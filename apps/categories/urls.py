from django.urls import path

from . import views

from apps.products.views import ProductDetailView


urlpatterns = [
    path('', views.CategoryListView.as_view(), name="category-list"),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name="category-detail"),
    path('<int:pk_category>/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
]