from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name="user-create"),
    path('favorite/', views.FavoriteListView.as_view(), name="favorite")
]