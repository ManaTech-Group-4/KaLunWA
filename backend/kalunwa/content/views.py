from django.db.models import Sum
from .models import CampEnum, Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (AnnouncementSerializer,  CabinOfficerSerializer, CampLeaderSerializer, 
                        CampPageSerializer, CommissionerSerializer, ContributorSerializer, 
                        DemographicsSerializer, EventSerializer,ImageSerializer, JumbotronSerializer,
                         OrgLeaderSerializer, ProjectSerializer, NewsSerializer) 
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from kalunwa.core.views import MultipleFieldLookupORMixin
from rest_framework.generics import (
    ListCreateAPIView
)


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['is_featured']
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else: 
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def update(self,request, pk):
    #     try:
    #         serializer_instance = self.queryset.get(id=pk)
    #     except Event.DoesNotExist:
    #         raise NotFound('Event with this ID does not exist.')
    #     data = self.serializer_class(instance=serializer_instance, data=request.data)
    
    #     if data.is_valid():
    #         data.save()
    #         return Response(data.data)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
'''
    def delete(self, request, pk):
        news = get_object_or_404(Event, id=pk)
        news.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        #returns http 204 no content, handle redirect or frontend?
'''
class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, CampFilter, QueryLimitBackend]
    filterset_fields = ['is_featured']
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def create(self, request):
    #     print(request.data)
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else: 
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self,request, pk):
    #     try:
    #         serializer_instance = self.queryset.get(id=pk)
    #     except Project.DoesNotExist:
    #         raise NotFound('Project with this ID does not exist.')
    #     data = self.serializer_class(instance=serializer_instance, data=request.data)
    
    #     if data.is_valid():
    #         data.save()
    #         return Response(data.data)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [ExcludeIDFilter, QueryLimitBackend]    
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except News.DoesNotExist:
            raise NotFound('News with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AnnouncementViewSet(viewsets.ModelViewSet):      
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = [QueryLimitBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except Announcement.DoesNotExist:
            raise NotFound('Announcement with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class JumbotronViewSet(viewsets.ModelViewSet):
    queryset = Jumbotron.objects.all()
    serializer_class = JumbotronSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend]
    filterset_fields = ['is_featured']   


class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer
    queryset = OrgLeader.objects.all()
    filter_backends = [OrgLeaderPositionFilter]
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #position only accepts KEY from choices enums eg. LDR
    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except OrgLeader.DoesNotExist:
            raise NotFound('Leader with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    #delete function default in viewsets

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()
    filter_backends = [CampFilter, CabinOfficerCategoryFilter]    
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #position only accepts KEY from choices enums eg. DIR
    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except CabinOfficer.DoesNotExist:
            raise NotFound('Leader with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()
    filter_backends = [CommissionerCategoryFilter]
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #position only accepts KEY from choices enums eg. CHF cat = GAE
    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except Commissioner.DoesNotExist:
            raise NotFound('Leader with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CampLeaderViewSet(viewsets.ModelViewSet): 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()
    filter_backends = [CampFilter, CampLeaderPositionFilter]
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]               

    #position only accepts KEY from choices enums eg. DIR
    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except CampLeader.DoesNotExist:
            raise NotFound('Leader with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CampPageViewSet(viewsets.ModelViewSet):
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [CampNameInFilter, QueryLimitBackend]   
    queryset = CampPage.objects.all()


class DemographicsViewSet(viewsets.ModelViewSet):
    serializer_class = DemographicsSerializer
    queryset = Demographics.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]               


    @action(detail=False, url_path='total-members')
    def total_members(self, request):
        return Response(Demographics.objects.aggregate(total_members=Sum('member_count')))

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk):
        try:
            serializer_instance = self.queryset.get(id=pk)
        except Demographics.DoesNotExist:
            raise NotFound('Municipality/City with this ID does not exist.')
        data = self.serializer_class(instance=serializer_instance, data=request.data)
    
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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



class EventGalleryListCreateView(ListCreateAPIView):
    """
    Allows the creation of an Image object directly to the related Event. 
    Will be called when the user wants to upload a new image in the gallery.
    """
    serializer_class = ImageSerializer
    lookup_fields = ['pk']

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

