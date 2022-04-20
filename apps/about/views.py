from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class AboutListView(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True, context={'request':request})
        return Response(serializer.data)
