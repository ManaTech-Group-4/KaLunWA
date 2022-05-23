from urllib import request
from django.db.models import Sum
from .models import Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (AnnouncementSerializer,  CabinOfficerSerializer, CampLeaderSerializer, 
                        CampPageSerializer, CommissionerSerializer, ContributorSerializer, 
                        DemographicsSerializer, EventSerializer,ImageSerializer, JumbotronSerializer,
                         OrgLeaderSerializer, ProjectSerializer, NewsSerializer) 
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, mixins
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from .filters import (
    QueryLimitBackend, 
    CampNameInFilter,
    OrgLeaderPositionFilter,
    CampFilter,
    CampLeaderPositionFilter,
    CommissionerCategoryFilter,
    CabinOfficerCategoryFilter,
    ExcludeIDFilter,
)

from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend] 
    filterset_fields = ['is_featured']


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend]
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


class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer
    queryset = OrgLeader.objects.all()
    filter_backends = [OrgLeaderPositionFilter]
              

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()
    filter_backends = [CampFilter, CabinOfficerCategoryFilter]    


class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()
    filter_backends = [CommissionerCategoryFilter]


class CampLeaderViewSet(viewsets.ModelViewSet): 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()
    filter_backends = [CampFilter, CampLeaderPositionFilter]               


class CampPageViewSet(viewsets.ModelViewSet):
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [CampNameInFilter, QueryLimitBackend]   
    queryset = CampPage.objects.all()


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
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        event_pk = self.request.query_params.get(f'has_event', None)      
        if event_pk is not None: 
            event = Event.objects.get(pk=event_pk).prefetch_related('gallery')
            return event.gallery.all()
        return super().get_queryset() 


class AnnouncementViewSet(viewsets.ModelViewSet):      
        serializer_class = AnnouncementSerializer
        queryset = Announcement.objects.all()
        filter_backends = [QueryLimitBackend]


class ImageUploadView(APIView): 
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''''
class AnnouncementCreateView(APIView): 

    def post(self, request, format=None):
        print(request.data)
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class AnnouncementListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = [QueryLimitBackend]

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
    def retrieve(self, request, ID):
        try:
            serializer_instance = self.queryset.get(id=ID)
        except Announcement.DoesNotExist:
            raise NotFound('Announcement with this ID does not exist.')

        serializer = self.serializer_class(serializer_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, ID):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(id=ID)
        except Announcement.DoesNotExist:
            raise NotFound('Announcement with this ID does not exist.')
            
        serializer_data = request.data.get('announcement', {})

        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CommentsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()

    def destroy(self, request, article_slug=None, comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            raise NotFound('A comment with this ID does not exist.')

        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''

class NewsListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [QueryLimitBackend]

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_backends = [QueryLimitBackend]

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = [QueryLimitBackend]

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)