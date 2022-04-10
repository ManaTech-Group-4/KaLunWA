
from django.db.models import Sum, Q
from .models import CampEnum, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import AboutUsCampSerializer, AboutUsLeaderImageSerializer, EventSerializer, HomepageEventSerializer,HomepageJumbotronSerializer, HomepageNewsSerializer, HomepageProjectSerializer, ImageSerializer, ImageURLSerializer, JumbotronSerializer, AnnouncementSerializer, ProjectSerializer, NewsSerializer
from .serializers import DemographicsSerializer, CampPageSerializer, OrgLeaderSerializer, CommissionerSerializer, CampLeaderSerializer, CabinOfficerSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


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

        serializer = AboutUsCampSerializer(camps, many=True, context={'request':request})
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
# -----------------------------------------------------------------------------    
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

        # expensive ata mo query from the /api/gallery (e.g. get images with related object)
        #     reasons:
        #         - querying for an image that is related to a camp, event and project
        #             - ?camp=<pk>&event=<pk>&project
        #             - queries from gallery record to see if image_id exists
        #             - individual queries to fetch related images from camp_id, event_id, and project_id,
        #               since all are in different tables (img.id,camp.id) - (img.id,event.id)
        #         - one table made as a junction table for all these records (w/ fields: img.id, camp.id, event.id etc.)
        #             does not have much of a use case as the other fields can be independent of the other

               
        # grab all the images, query for their related objects (projects, events, camps)
        # image_id
        # event_id
        # project_id
        # camp_id

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
        # case -> no related images, return null or empty list? -> list 



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

class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()




# ------------------------------------------------------------------------------
# to be removed if approved
#-------------------------------------------------------------------------------
# homepage views


class HomepageViewSet(viewsets.ViewSet):

    @action(detail=False)
    def jumbotrons(self, request):
        jumbotrons = Jumbotron.objects.all()[:5] # need is_featured?
        # passing context from the request, for the serializer to use
        serializer = HomepageJumbotronSerializer(jumbotrons, many=True, context={'request':request})
        return Response(serializer.data)

    @action(detail=False)
    def events(self, request):
        events = Event.objects.filter(is_featured=True)[:3]
        serializer = HomepageEventSerializer(events, many=True,context={'request':request})
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
    def camps(self, request): # is_about=True -> return these? 
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
        """
        return only people from execomm -> pres to overseer
        """
        org_leaders = OrgLeader.objects.exclude(              #  is_execomm? -> custom filter
            Q(position=OrgLeader.Positions.DIRECTOR.value) |
            Q(position=OrgLeader.Positions.OTHER.value)
            )
        serializer = AboutUsLeaderImageSerializer(org_leaders, many=True, context={'request':request})
        return  Response(serializer.data)


#------------------------------------------------------- 
    