from rest_framework.routers import DefaultRouter

from .views import ImageViewSet, JumbotronViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
urlpatterns = router.urls
