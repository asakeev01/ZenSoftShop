from rest_framework.views import APIView

from .models import *
from .serializers import *
from .paginators import *


class NewsListView(APIView):

    def get(self, request):
        news = News.objects.all()
        paginator = NewsPaginator()
        news_page = paginator.paginate_queryset(news, request)
        news_ser = NewsSerializer(news_page, many=True, context={'request': request})
        return paginator.get_paginated_response(news_ser.data)