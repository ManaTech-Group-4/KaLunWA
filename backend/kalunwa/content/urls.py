from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AnnouncementViewSet, 
    CabinOfficerViewSet, 
    CampLeaderViewSet,
    CampPageGalleryListCreateView, 
    CampPageViewSet, 
    CommissionerViewSet, 
    DemographicsViewSet, 
    EventViewSet, 
    ImageViewSet, 
    JumbotronViewSet, 
    NewsViewSet, 
    OrgLeaderViewSet, 
    ProjectViewSet, 
    )
 

router = DefaultRouter()

# for complete detail
router.register(r'gallery', ImageViewSet, basename='image')
router.register(r'jumbotrons', JumbotronViewSet, basename='jumbotron')
router.register(r'events', EventViewSet, basename='event')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')

router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'demographics', DemographicsViewSet, basename='demographics')
router.register(r'orgleaders', OrgLeaderViewSet, basename='orgleader')
router.register(r'commissioners', CommissionerViewSet, basename='commissioner')
router.register(r'campleaders', CampLeaderViewSet, basename='campleader')
router.register(r'cabinofficers', CabinOfficerViewSet, basename='cabinofficer')
urlpatterns = router.urls

"""
instead of: 
    router.register(r'camps', CampPageViewSet, basename='camp')
we are to map the patterns manually, given we want to be capable of doing
multiple look-u fields. 
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
    path('camps/<int:pk>/gallery/', CampPageGalleryListCreateView.as_view(), name='camp-gallery-list'),
    path('camps/<slug:slug>/gallery/', CampPageGalleryListCreateView.as_view(), name='camp-gallery-list'),    
]