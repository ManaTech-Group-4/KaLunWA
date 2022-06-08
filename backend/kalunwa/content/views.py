from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db.models import Sum
from django.forms import ValidationError
from .models import Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (
    AnnouncementSerializer,
    CabinOfficerSerializer, 
    CampLeaderSerializer, 
    CampPageSerializer, 
    CommissionerSerializer, 
    ContributorSerializer, 
    DemographicsSerializer, 
    EventSerializer,
    ImageSerializer, 
    JumbotronSerializer,
    OrgLeaderSerializer,
    ProjectSerializer,
    NewsSerializer,
) 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
)
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
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
from kalunwa.core.views import MultipleFieldLookupORMixin
    
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


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = [QueryLimitBackend]


class ImageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    serializer_class = ImageSerializer
    # prefetched so that related objects are cached, and query only hits db once
    queryset = Image.objects.all()


class CampPageGalleryListCreateView(MultipleFieldLookupORMixin, ListCreateAPIView):
    """
    Allows the creation of an Image object directly to the related Camp. 
    Will be called when the user wants to upload a new image in the gallery.
    """
    serializer_class = ImageSerializer
    lookup_fields = ['id', 'slug']

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