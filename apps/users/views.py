from .serializers import *
from .models import *


from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserCreateSerializer