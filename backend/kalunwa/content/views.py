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
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, ChoiceFilter, CharFilter
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
        if limit is None or not limit.isdigit():
            return queryset
        limit = int(limit)
        return queryset[:limit]

    def limit_related_gallery(self, queryset,request, limit, model):
        """
        use for models that have gallery implementations.
        viewsets should have a 'model' attribute set. 

        quick docs:
        sub_query
            (1) gets related images of a content where imageA's event is in [imageB's]
             where imageA is an image from an content's gallery (content
                  had been selected/reduced e.g. is_featured filter), and
            imageB is an image from the big set (Image.obj.all())     
                                
        (1) OuterRef -> refers to a field from the main query at Prefetch (3) 
        (2) values_list and flat=True (returns list of pks)
            return a QuerySet of single values instead of 1-tuples:
                e.g. <QuerySet [1, 2]>     
        (3) Prefetch -> extends prefetch_related by specifying queryset (qs)
            in this case, it limits the qs to the images belonging to a content's gallery,
            to which its number is limited to `query_limit_gallery`

        (4) add `distinct` since duplicate image objs are returned for images
             belonging in more than 1 gallery given a many-to-many relationship                       
        """
        if limit is None or not limit.isdigit():
            return queryset
        limit = int(limit)
        # related_name -> gallery_<content> -> format via user
        related_name = model._meta.get_field('gallery').related_query_name()
        # gallery_events__in=OuterRef('gallery_events') -> in filter (1)
        kwargs = {f'{related_name}__in': OuterRef(related_name)} 
        sub_query = Subquery(Image.objects
                    .prefetch_related(related_name) 
                    .filter(**kwargs) # 1
                    .values_list('id', flat=True)[:limit] # 2               
                    ) 
        prefetch = Prefetch('gallery', # 3
            queryset=Image.objects.filter(id__in=sub_query).distinct()) # 4
        return queryset.prefetch_related(prefetch)        


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

# organization structure

class LabelToValue:
    def get_value_by_label(self, label:str, Enum): 
        if not label in Enum.labels:
            return None

        for enum_obj in Enum.__members__.values(): # enum members -> key:name, value:enum_obj { 'PRESIDENT': OrgLeader.Positions.PRESIDENT }
            if label == enum_obj.label: 
                value = enum_obj.value
        return value


class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer

    def get_queryset(self):
        # or make custom filter
        get_position = self.request.query_params.get('position')  
        if get_position=="ExeComm":          
            execomm_leaders = OrgLeader.objects.exclude(              #  is_execomm? -> custom filter
            Q(position=OrgLeader.Positions.DIRECTOR.value) |
            Q(position=OrgLeader.Positions.OTHER.value)
            )
            return execomm_leaders
        if get_position == None:
            return OrgLeader.objects.all()
        else:
            get_position_value = LabelToValue().get_value_by_label(get_position,OrgLeader.Positions)
            return OrgLeader.objects.filter(position=get_position_value)


class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer

    def get_queryset(self):
        get_camp = self.request.query_params.get('camp')
        get_category = self.request.query_params.get('category') 
        camp_value = LabelToValue().get_value_by_label(get_camp,CampEnum)
        category_value = LabelToValue().get_value_by_label(get_category,CabinOfficer.Categories)
        if get_camp is not None and get_category == None:
            return CabinOfficer.objects.filter(camp=camp_value)
        if get_camp == None and get_category is not None:
            return CabinOfficer.objects.filter(category=category_value)   
        if get_camp is not None and get_category is not None:
            return CabinOfficer.objects.filter(camp=camp_value, category=category_value)
        else:
            return CabinOfficer.objects.all()


class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer

    def get_queryset(self):
        get_category = self.request.query_params.get('category') 
        if get_category== None:
            return Commissioner.objects.all()
        else:
            category_value = LabelToValue().get_value_by_label(get_category,Commissioner.Categories)
            return Commissioner.objects.filter(category=category_value)


# prep for about us
class CampLeaderViewSet( viewsets.ModelViewSet): # limit 1 per query 
    serializer_class = CampLeaderSerializer
    

    def get_queryset(self):
        get_camp = self.request.query_params.get('camp') 
        if get_camp== None:
            return CampLeader.objects.all()
        else:
            camp_value = LabelToValue().get_value_by_label(get_camp,CampEnum)
            return CampLeader.objects.filter(camp=camp_value)


class CampNameInFilterBackend(BaseFilterBackend):
    """
    # expect a list of names here. (e.g. Suba,Lasang,)
    # urls don't accept whitespaces, so don't have to worry bout that 
    # spaces are automatically replaced with `%20`
    # risky inputs
    #   Suba,,,,General,, -> would be accepted (same behavior for flex fields)

    """

    def filter_queryset(self, request, queryset, view):
        name_labels = request.query_params.get('name__in', None)     
        if name_labels is None:
            return queryset
        return self.filter_by_names(queryset, name_labels)

    def get_name_values(self, name_labels:str): # returns a list of camp values ['SB', Lasang]
        camp_values = []
        for label in name_labels.split(','):
           camp_value = get_value_by_label(label, CampEnum)
           if camp_value is None: # not valid camp_label so skip value
              pass  
           else:
               camp_values.append(camp_value)
        return camp_values     

    def filter_by_names(self, queryset, name_labels:str):
        camp_values = self.get_name_values(name_labels)
        return queryset.filter(name__in=camp_values)              

def get_value_by_label(label:str, Enum): # will prolly be put in core/utils
    if not label in Enum.labels:
        return None
    for enum_obj in Enum.__members__.values(): # enum members -> key:name-value:enum_obj { 'PRESIDENT': OrgLeader.Positions.PRESIDENT }
        if label == enum_obj.label: 
            value = enum_obj.value
    return value


class CampPageViewSet(viewsets.ModelViewSet):
    model = CampPage
    serializer_class = CampPageSerializer
    filter_backends = [CampNameInFilterBackend, QueryLimitBackend]   
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


