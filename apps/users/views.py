from .serializers import *
from .models import *

from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class FavoriteListView(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, **kwargs):
        favorite = Favorite.objects.get(user=self.request.user)
        return favorite
    serializer_class = FavoriteSerializer