from rest_framework.routers import DefaultRouter

from .views import ImageViewSet, JumbotronViewSet, AnnouncementViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'announcements', AnnouncementViewSet,basename='announcement' )
urlpatterns = router.urls
