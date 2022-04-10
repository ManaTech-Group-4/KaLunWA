
from django.db.models import Sum
from .models import CampEnum, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import AboutUsCampSerializer, AboutUsLeaderImageSerializer, EventSerializer,HomepageJumbotronSerializer, HomepageNewsSerializer, HomepageProjectSerializer, ImageSerializer, ImageURLSerializer, JumbotronSerializer, AnnouncementSerializer, ProjectSerializer, NewsSerializer
from .serializers import DemographicsSerializer, CampPageSerializer, OrgLeaderSerializer, CommissionerSerializer, CampLeaderSerializer, CabinOfficerSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


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


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_featured']


class ReturnRelatedObjectsMixin:
    def get_queryset(self):
        pass



class ImageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    serializer_class = ImageSerializer
    queryset = Image.objects.prefetch_related('gallery_events', 'gallery_projects', 'gallery_camps') 
    filter_backends = [DjangoFilterBackend]
    related_objects = ['has_event']

    def get_queryset(self):
        event_pk = self.request.query_params.get(f'has_event', None)      
        # get event
        if event_pk is not None: 
            event = Event.objects.get(pk=event_pk).prefetch_related('gallery')
            return event.gallery.all()
        
        # grab all the images, query for their related objects (projects, events, camps)
        # image_id
        # event_id
        # project_id
        # camp_id

        return super().get_queryset()
    # return images where event_id is in events.id
    # change queryset according to an event_id
        # returns event_id.gallery

    # has_event=1
        # get has_event
        # in gallery
            # get event with pk 
            # return objects related to event via event.gallery()

        # cases -> event does not exist
            # return none or error? -> error 
        # case -> no related images, return null or empty list? 



#-------------------------------------------------------------------------------
# homepage views



class HomepageViewSet(viewsets.ViewSet):

    @action(detail=False)
    def jumbotrons(self, request):
        jumbotrons = Jumbotron.objects.all()
        # passing context from the request, for the serializer to use
        serializer = HomepageJumbotronSerializer(jumbotrons, many=True, context={'request':request})
        return Response(serializer.data)

    @action(detail=False)
    def projects(self, request):
        projects = Project.objects.filter(is_featured=True)[:3]
        serializer = HomepageProjectSerializer(projects, many=True,context={'request':request})
        return Response(serializer.data)    
    
    @action(detail=False)
    def news(self, request):
        news = News.objects.order_by('-created_at')[:3]
        serializer = HomepageNewsSerializer (news, many=True,context={'request':request})
        return Response(serializer.data)    

#-------------------------------------------------------------------------------
# about us view

class AboutUsViewset(viewsets.ViewSet): # leaders
    @action(detail=False)
    def demographics(self, request):
        return Response(Demographics.objects.aggregate(total_members=Sum('member_count')))
    
    @action(detail=False)
    def camps(self, request):
        # ensures 1 of each camp incase of duplicates
        suba = CampPage.objects.filter(name=CampEnum.SUBA) [:1]
        baybayon = CampPage.objects.filter(name=CampEnum.BAYBAYON) [:1]
        zero_waste = CampPage.objects.filter(name=CampEnum.ZEROWASTE) [:1]
        lasang = CampPage.objects.filter(name=CampEnum.LASANG) [:1]

        camps = suba | baybayon | zero_waste | lasang # combines into one queryset

        serializer = AboutUsCampSerializer(camps, many=True, context={'request':request})
        return Response(serializer.data)
    
    @action(detail=False)
    def organization_leaders(self, request):
        org_leaders = OrgLeader.objects.all()[:5]
        serializer = AboutUsLeaderImageSerializer(org_leaders, many=True, context={'request':request})
        return  Response(serializer.data)


#------------------------------------------------------- 




class JumbotronViewSet(viewsets.ModelViewSet):
    serializer_class = JumbotronSerializer
    queryset = Jumbotron.objects.all()

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    

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

class DemographicsViewSet(viewsets.ModelViewSet):
    serializer_class = DemographicsSerializer
    queryset = Demographics.objects.all()

class CampPageViewSet(viewsets.ModelViewSet):
    serializer_class = CampPageSerializer
    queryset = CampPage.objects.all()

class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer
    queryset = OrgLeader.objects.all()

class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()

class CampLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()