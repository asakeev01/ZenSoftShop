from .views import CategoryViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='category')
urlpatterns = router.urls