from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('', views.MainListView.as_view(), name="main-list"),
    path('faq/', views.FAQListView.as_view(), name="faq"),
    path('header/', views.HeaderListView.as_view(), name="header"),
    path('public/', views.PublicListView.as_view(), name="public"),
    path('url/', views.UrlListView.as_view(), name="url")
]

router = DefaultRouter()
router.register(r'request', views.RequestViewSet, basename='request')
urlpatterns += router.urls