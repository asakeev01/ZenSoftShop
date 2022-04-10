from . import settings

from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/categories/', include('apps.categories.urls')),
    path('api/main/', include('apps.main.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
