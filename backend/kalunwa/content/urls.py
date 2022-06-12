from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AnnouncementViewSet, 
    CabinOfficerViewSet, 
    CampLeaderViewSet,
    CampPageViewSet, 
    CommissionerViewSet, 
    DemographicsViewSet, 
    EventViewSet, 
    ImageViewSet, 
    JumbotronViewSet, 
    NewsViewSet, 
    OrgLeaderViewSet,
    ProjectViewSet, 
    CampPageGalleryListCreateView,
    ProjectGalleryListCreateView,     
    EventGalleryListCreateView,   
    ContributorViewset, 
)

router = DefaultRouter()

# for complete detail
router.register(r'gallery', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'camps', CampPageViewSet, basename='camp')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'demographics', DemographicsViewSet, basename='demographics')
router.register(r'orgleaders', OrgLeaderViewSet, basename='orgleader')
router.register(r'commissioners', CommissionerViewSet, basename='commissioner')
router.register(r'campleaders', CampLeaderViewSet, basename='campleader')
router.register(r'cabinofficers', CabinOfficerViewSet, basename='cabinofficer')
router.register(r'contributors', ContributorViewset, basename='contributor')
urlpatterns = router.urls

urlpatterns += [
    # gallery implementations
    path('events/<int:pk>/gallery/', EventGalleryListCreateView.as_view(), name='event-gallery-list'),
   path('projects/<int:pk>/gallery/', ProjectGalleryListCreateView.as_view(), name='project-gallery-list'),    
   path('camps/<int:pk>/gallery/', CampPageGalleryListCreateView.as_view(), name='camp-gallery-list'),
    path('camps/<slug:slug>/gallery/', CampPageGalleryListCreateView.as_view(), name='camp-gallery-list'),      
   # add image to contributor directly 
]

"""
instead of: 
    router.register(r'camps', CampPageViewSet, basename='camp')
we are to map the url patterns manually, given we want to be capable of doing
multiple look-u fields (detail via id and slug). 
"""

urlpatterns += [
    path('camps/', CampPageViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }, 
            ), name = 'camp-list'  
    ),
    path('camps/<int:pk>/', CampPageViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            ), name = 'camp-detail'              
    ),
    path('camps/<slug:slug>/', CampPageViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            ), name = 'camp-detail'              
    ),    
]