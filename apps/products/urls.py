from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name = "product-list"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name = "product-detail"),
    path('<int:pk>/items/', views.ProductItemListView.as_view(), name = "product-items-list")
]