from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db.models import Sum
from kalunwa.core.views import MultipleFieldLookupORMixin
from .models import Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (AnnouncementSerializer,  CabinOfficerSerializer, CampLeaderSerializer, 
                        CampPageSerializer, CommissionerSerializer, ContributorSerializer, 
                        DemographicsSerializer, EventSerializer,ImageSerializer, JumbotronSerializer,
                         OrgLeaderSerializer, ProjectSerializer, NewsSerializer) 
from rest_framework.response import Response
from rest_framework import viewsets, status
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

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView
)
from django.contrib.auth.models import AnonymousUser


class AssignLastUpdatedBy:
    def assign_editor(self, instance):
        """ after applying serializer changes, assign user and save. """
        if not (self.request.user is AnonymousUser):
            # anonymous user is returned in open views (dont need auth)
            instance.last_updated_by = self.request.user
            instance.save()

    def perform_create(self, serializer):
        """
        Override perform create to allow the assignment of the user after it had 
        been successfully saved.
        Cannot be done in signals since it cannot access requests, given edits
        are done model-level only.
        """
        # instance is created here, and signals the presave. 
        # presave check if it exists, which it does not since it's the creation process
        instance = serializer.save()
        # after it's created, it gets assigned then.
        self.assign_editor(instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        self.assign_editor(instance)    

    
class EventViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['is_featured']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]    
    filterset_fields = ['is_featured']


class NewsViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [ExcludeIDFilter, QueryLimitBackend]    
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnnouncementViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):      
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = [QueryLimitBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]



class JumbotronViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    queryset = Jumbotron.objects.all()
    serializer_class = JumbotronSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend]
    filterset_fields = ['is_featured']   


class OrgLeaderViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer
    queryset = OrgLeader.objects.all()
    filter_backends = [OrgLeaderPositionFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]



class CabinOfficerViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()
    filter_backends = [CampFilter, CabinOfficerCategoryFilter]    
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommissionerViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()
    filter_backends = [CommissionerCategoryFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CampLeaderViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet): 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()
    filter_backends = [CampFilter, CampLeaderPositionFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]               


class CampPageViewSet(AssignLastUpdatedBy, MultipleFieldLookupORMixin, viewsets.ModelViewSet): 
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [CampNameInFilter, QueryLimitBackend]   
    queryset = CampPage.objects.all()
    lookup_fields = ['id', 'slug']
    permission_classes = [IsAuthenticatedOrReadOnly]      


class DemographicsViewSet(AssignLastUpdatedBy,viewsets.ModelViewSet):
    serializer_class = DemographicsSerializer
    queryset = Demographics.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]               

    @action(detail=False, url_path='total-members')
    def total_members(self, request):
        return Response(Demographics.objects.aggregate(total_members=Sum('member_count')))


class ContributorViewset(AssignLastUpdatedBy, viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]                   
# -----------------------------------------------------------------------------    

class ImageViewSet(AssignLastUpdatedBy, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    serializer_class = ImageSerializer
    # prefetched so that related objects are cached, and query only hits db once
    queryset = Image.objects.prefetch_related('gallery_events', 'gallery_projects', 'gallery_camps') 
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]                   

    def get_queryset(self):
        event_pk = self.request.query_params.get(f'has_event', None)      
        if event_pk is not None: 
            event = Event.objects.get(pk=event_pk).prefetch_related('gallery')
            return event.gallery.all()
        return super().get_queryset() 


class EventGalleryListCreateView(ListCreateAPIView):
    """
    Allows the creation of an Image object directly to the related Event. 
    Will be called when the user wants to upload a new image in the gallery.
    """
    serializer_class = ImageSerializer
    lookup_fields = ['pk']
    permission_classes = [IsAuthenticatedOrReadOnly]               

    def get_event_object(self):
        event_id = self.kwargs['pk']
        print(event_id)
        return get_object_or_404(Event, pk=event_id)

    def get_queryset(self): # get list of images related to the event
        event = self.get_event_object()
        return event.gallery 

    def perform_link_image_to_event(self, image:int):
        """
        automatically add image to the gallery of the event upon implementing.
        """
        event = self.get_event_object()
        event.gallery.add(image)        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        image = Image.objects.get(
            id = serializer.data['id']    
        )
        self.perform_link_image_to_event(image)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectGalleryListCreateView(ListCreateAPIView):
    """
    Allows the creation of an Image object directly to the related Project. 
    Will be called when the user wants to upload a new image in the gallery.
    """
    serializer_class = ImageSerializer
    lookup_fields = ['pk']
    permission_classes = [IsAuthenticatedOrReadOnly]        

    def get_project_object(self):
        project_id = self.kwargs['pk']
        print(project_id)
        return get_object_or_404(Project, pk=project_id)

    def get_queryset(self): # get list of images related to the project
        project = self.get_project_object()
        return project.gallery 

    def perform_link_image_to_project(self, image:int):
        """
        automatically add image to the gallery of the project upon implementing.
        """
        project = self.get_project_object()
        project.gallery.add(image)        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        image = Image.objects.get(
            id = serializer.data['id']    
        )
        self.perform_link_image_to_project(image)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CampPageGalleryListCreateView(MultipleFieldLookupORMixin, ListCreateAPIView):
    """
    Allows the creation of an Image object directly to the related Camp. 
    Will be called when the user wants to upload a new image in the gallery.
    """
    serializer_class = ImageSerializer
    lookup_fields = ['id', 'slug']
    permission_classes = [IsAuthenticatedOrReadOnly]        

    def get_camp_object(self):
        for field in self.lookup_fields:
            try:                                  # Get the result with one or more fields.
                look_up_value = self.kwargs[field]
                kwargs = {f'{field}' : look_up_value}                 
                return CampPage.objects.get(**kwargs)
            except KeyError: # Key error, look up field not in url 
                pass
        raise NotFound(detail="Camp page does not exist.", code=status.HTTP_404_NOT_FOUND)

    def get_queryset(self): # get list of images related to the camp
        camp = self.get_camp_object()
        return camp.gallery 

    def perform_link_image_to_camp(self, image:int):
        """
        automatically add image to the gallery of the camp upon implementing.
        """
        camp = self.get_camp_object()
        camp.gallery.add(image)        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        image = Image.objects.get(
            id = serializer.data['id']    
        )
        self.perform_link_image_to_camp(image)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        
class ImageUploadView(APIView): 
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]        

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

