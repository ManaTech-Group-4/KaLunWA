from rest_framework.routers import DefaultRouter

from .views import EventViewSet, ImageViewSet, JumbotronViewSet, ProjectViewSet, NewsViewSet, AnnouncementViewSet,  HomepageViewSet

router = DefaultRouter()

router.register(r'homepage', HomepageViewSet, basename='homepage')

# /jumbotron/homepage_info
# /homepage_jumbotrons
# /homepage_events
# /homepage_projects
# /homepage_news

# for complete detail
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
urlpatterns = router.urls
