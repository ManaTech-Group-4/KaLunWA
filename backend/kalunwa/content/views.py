from django.db.models import Sum, Q, OuterRef, Subquery, Prefetch
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
from rest_framework.filters import BaseFilterBackend


class QueryLimitBackend(BaseFilterBackend):
    """
    Backend filters are done from left to right, so ensure that this is put
    at the very right of the list. This is because a queryset cannot be filtered 
    further after splicing it (e.g. queryset[:limit]). 
    ps: may be useless when post and validation is implemented.

    e.g. [DjangoFilter, ..., QueryLimitBackend]

    note: put related names on the viewset.
    """
    def filter_queryset(self, request, queryset, view):
        query_limit = request.query_params.get('query_limit', None)        
        if view.action in ['list'] and query_limit is not None:
            queryset = self.limit_query(queryset, request, query_limit)

        query_limit_gallery = request.query_params.get('query_limit_gallery', None)            
        if view.action in ['list', 'retrieve'] \
            and query_limit_gallery is not None:          
            queryset = self.limit_related_gallery(queryset, request, 
                        query_limit_gallery, view.model)
        return queryset

    def limit_query(self, queryset, request, limit):
        if limit is not None and limit.isdigit():
            limit = int(limit)
            queryset = queryset[:limit]
            
        return queryset

    def limit_related_gallery(self, queryset,request, limit, model):
        """
        use for models that have gallery implementations.
        viewsets should have a 'model' attribute set. 
        """
        if limit is not None and limit.isdigit():
            limit = int(limit)
            # related_name -> gallery_<content> -> format via user
            related_name = model._meta.get_field('gallery').related_query_name()
            # sub_query
               # (1) gets related images of a content where imageA's event is in [imageB's]
                #  where imageA is an image from an content's gallery (content
                #       had been selected/reduced e.g. is_featured filter), and
                # imageB is an image from the big set (Image.obj.all())     
                                  
            # (1) OuterRef -> refers to a field from the main query at Prefetch (3) 
            # (2) values_list and flat=True (returns list of pks)
                # return a QuerySet of single values instead of 1-tuples:
                    # e.g. <QuerySet [1, 2]>    
            kwargs = {f'{related_name}__in': OuterRef(related_name)} 
                      # gallery_events__in=OuterRef('gallery_events') -> in filter (1)
            sub_query = Subquery(Image.objects
                        .prefetch_related(related_name) 
                        .filter(**kwargs) # 1
                        .values_list('id', flat=True)[:limit] # 2               
                        ) 

            # (3) Prefetch -> extends prefetch_related by specifying queryset (qs)
                # in this case, it limits the qs to the images belonging to a content's gallery,
                # to which its number is limited to `query_limit_gallery`

            # (4) add `distinct` since duplicate image objs are returned for images
                #  belonging in more than 1 gallery given a many-to-many relationship
            prefetch = Prefetch('gallery', # 3
                queryset=Image.objects.filter(id__in=sub_query).distinct()) # 4

            queryset = queryset.prefetch_related(prefetch) 

        return queryset


class EventViewSet( viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all() # prefetch_related
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend] 
    filterset_fields = ['is_featured']


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend]
    filterset_fields = ['is_featured']


class JumbotronViewSet(viewsets.ModelViewSet):
    queryset = Jumbotron.objects.all()
    serializer_class = JumbotronSerializer
    filter_backends = [DjangoFilterBackend, QueryLimitBackend]
    filterset_fields = ['is_featured']   


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [QueryLimitBackend]    
    serializer_class = NewsSerializer
    

# prep for about us
class CampLeaderViewSet(viewsets.ModelViewSet): # limit 1 per query 
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()


class CampPageViewSet(viewsets.ModelViewSet):
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [QueryLimitBackend]        

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