from rest_framework.routers import DefaultRouter

from .views import AboutUsViewset, EventViewSet, ImageViewSet, JumbotronViewSet, ProjectViewSet, NewsViewSet, AnnouncementViewSet,  HomepageViewSet
from .views import DemographicsViewSet, CampPageViewSet, OrgLeaderViewSet, CommissionerViewSet, CampLeaderViewSet, CabinOfficerViewSet

router = DefaultRouter()

router.register(r'homepage', HomepageViewSet, basename='homepage')
router.register(r'about-us', AboutUsViewset, basename='about-us')

# for complete detail
router.register(r'images', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'demographics', DemographicsViewSet, basename='demographic')
router.register(r'camppages', CampPageViewSet, basename='camp')
router.register(r'orgleaders', OrgLeaderViewSet, basename='orgleader')
router.register(r'commissioners', CommissionerViewSet, basename='commissioner')
router.register(r'campleaders', CampLeaderViewSet, basename='campleader')
router.register(r'cabinofficers', CabinOfficerViewSet, basename='cabinofficer')
urlpatterns = router.urls
