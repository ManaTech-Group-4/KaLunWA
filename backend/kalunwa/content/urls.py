from rest_framework.routers import DefaultRouter

from .views import EventViewSet, HomepageJumbotronViewSet, ImageViewSet, JumbotronViewSet, AnnouncementViewSet

router = DefaultRouter()

# for homepage onlies
router.register(r'homepage-jumbotrons', HomepageJumbotronViewSet, basename='homepage-jumbotron')



# for complete detail
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'announcements', AnnouncementViewSet, basename='announcement' )
router.register(r'events', EventViewSet, basename='event' )
urlpatterns = router.urls
