from django.db.models import Sum, Q
from .models import CampEnum, Contributor, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import (AnnouncementSerializer,  CabinOfficerSerializer, CampLeaderSerializer, 
                        CampPageSerializer, CommissionerSerializer, ContributorSerializer, 
                        DemographicsSerializer, EventSerializer,ImageSerializer, JumbotronSerializer,
                         OrgLeaderSerializer, ProjectSerializer, NewsSerializer) 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser

class QueryLimitViewMixin:

    def finalize_response(self, request, response, *args, **kwargs):
        """
        Limits the number of records returned. 
        """
        if self.action=='list':
            query_limit = self.request.query_params.get('query_limit', None)
            if query_limit is not None and query_limit.isdigit():
                query_limit = int(query_limit)
                response.data = response.data[:query_limit]

        return super().finalize_response(request, response, *args, **kwargs)


class EventViewSet(QueryLimitViewMixin, viewsets.ModelViewSet): 
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_featured']
    # might need to add new serializer field for non-read only stuff that needs
    # to be posted data on (or let frontend manipulate the dates nlng)


class ProjectViewSet(QueryLimitViewMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_featured']


class JumbotronViewSet(QueryLimitViewMixin, viewsets.ModelViewSet):
    queryset = Jumbotron.objects.all()
    serializer_class = JumbotronSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_featured']   


class NewsViewSet(QueryLimitViewMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [OrderingFilter]    
    odering_fields = ['created_at']
    

# prep for about us
class CampLeaderViewSet(viewsets.ModelViewSet): # limit 1 per query 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()


class CampPageViewSet(viewsets.ModelViewSet):
    serializer_class = CampPageSerializer

    def get_queryset(self):
        # if preferred -> pure url search 
        if self.action=='list':
            one_each_flag = self.request.query_params.get('one_each', False)
            # one_each ensures a limit of 1 instance per camp except general
            if one_each_flag:
                suba = CampPage.objects.filter(name=CampEnum.SUBA) [:1]
                baybayon = CampPage.objects.filter(name=CampEnum.BAYBAYON) [:1]
                zero_waste = CampPage.objects.filter(name=CampEnum.ZEROWASTE) [:1]
                lasang = CampPage.objects.filter(name=CampEnum.LASANG) [:1]
                camps = suba | baybayon | zero_waste | lasang # combines into one queryset
                return camps

        return CampPage.objects.all()

    @action(detail=False, url_path='about-us')
    def about_us(self, request): 
        # alternatives:
            # provide one_each=True to query string to return this 
        # ensures 1 of each camp incase of duplicates
        suba = CampPage.objects.filter(name=CampEnum.SUBA) [:1]
        baybayon = CampPage.objects.filter(name=CampEnum.BAYBAYON) [:1]
        zero_waste = CampPage.objects.filter(name=CampEnum.ZEROWASTE) [:1]
        lasang = CampPage.objects.filter(name=CampEnum.LASANG) [:1]

        camps = suba | baybayon | zero_waste | lasang # combines into one queryset

        serializer = CampPageSerializer(camps, many=True, context={'request':request})
        return Response(serializer.data)


class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer

    def get_queryset(self):
        # or make custom filter
        if self.action=='list':
            is_execomm = self.request.query_params.get('is_execomm', False)  
            if is_execomm:          
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
    parser_classes = (MultiPartParser, FormParser)




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