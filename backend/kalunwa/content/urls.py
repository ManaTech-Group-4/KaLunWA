from rest_framework.routers import DefaultRouter

from .views import EventViewSet, ImageViewSet, JumbotronViewSet, ProjectViewSet, NewsViewSet, AnnouncementViewSet,  HomepageViewSet
from .views import DemographicsViewSet, CampPageViewSet, OrgLeaderViewSet, CampOfficerViewSet

router = DefaultRouter()

router.register(r'homepage', HomepageViewSet, basename='homepage')

# for complete detail
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'demographics', DemographicsViewSet, basename='announcement')
router.register(r'camppage', CampPageViewSet, basename='announcement')
router.register(r'orgleader', OrgLeaderViewSet, basename='announcement')
router.register(r'campofficer', CampOfficerViewSet, basename='announcement')
urlpatterns = router.urls
