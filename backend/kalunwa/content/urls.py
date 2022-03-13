from rest_framework.routers import DefaultRouter

from .views import EventViewSet, ImageViewSet, JumbotronViewSet, AnnouncementViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'announcements', AnnouncementViewSet, basename='announcement' )
router.register(r'events', EventViewSet, basename='event' )
urlpatterns = router.urls
