from django.db.models import Sum, Q
from .models import Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (AnnouncementSerializer,  CabinOfficerSerializer, CampLeaderSerializer, 
                        CampPageSerializer, CommissionerSerializer, ContributorSerializer, 
                        DemographicsSerializer, EventSerializer,ImageSerializer, JumbotronSerializer,
                         OrgLeaderSerializer, ProjectSerializer, NewsSerializer) 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExcludeIDFilter, QueryLimitBackend, CampNameInFilterBackend


class EventViewSet( viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend,ExcludeIDFilter, QueryLimitBackend] 
    filterset_fields = ['is_featured']


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend,ExcludeIDFilter, QueryLimitBackend]
    filterset_fields = ['is_featured']


class JumbotronViewSet(viewsets.ModelViewSet):
    queryset = Jumbotron.objects.all()
    serializer_class = JumbotronSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend]
    filterset_fields = ['is_featured']   


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [ExcludeIDFilter, QueryLimitBackend]    
    serializer_class = NewsSerializer
    

# prep for about us
class CampLeaderViewSet(viewsets.ModelViewSet): # limit 1 per query 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()


class CampPageViewSet(viewsets.ModelViewSet):
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [CampNameInFilterBackend, QueryLimitBackend]   
    queryset = CampPage.objects.all()


class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer

    def get_queryset(self):
        # or make custom filter
        if self.action=='list':
            position = self.request.query_params.get('position', None)  
            if position is not None:          
                execomm_leaders = OrgLeader.objects.exclude(              #  is_execomm? -> custom filter
                Q(position=OrgLeader.Positions.DIRECTOR.value) |
                Q(position=OrgLeader.Positions.OTHER.value)
                )
                return execomm_leaders

        return OrgLeader.objects.all()


class DemographicsViewSet(viewsets.ModelViewSet):
    serializer_class = DemographicsSerializer
    queryset = Demographics.objects.all()

    @action(detail=False, url_path='total-members')
    def total_members(self, request):
        return Response(Demographics.objects.aggregate(total_members=Sum('member_count')))


class ContributorViewset(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()

# -----------------------------------------------------------------------------    
# tester for gallery 
class ImageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    serializer_class = ImageSerializer
    # prefetched so that related objects are cached, and query only hits db once
    queryset = Image.objects.prefetch_related('gallery_events', 'gallery_projects', 'gallery_camps') 
    related_objects = ['has_event']

    def get_queryset(self):
        event_pk = self.request.query_params.get(f'has_event', None)      
        if event_pk is not None: 
            event = Event.objects.get(pk=event_pk).prefetch_related('gallery')
            return event.gallery.all()
        return super().get_queryset() 


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


#-------------------------------------------------------
# Prep for file uploading
# 
# class ImageUploadView(APIView): 
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
# #        print(request.data)
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else: 
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-----------------------------newly added models as of 23/3/2022-------------------------------------------------


class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()    