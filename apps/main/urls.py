from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainListView.as_view(), name="main-list"),
]