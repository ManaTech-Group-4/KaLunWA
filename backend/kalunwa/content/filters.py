from django.db.models import Q, OuterRef, Subquery, Prefetch
from rest_framework.filters import BaseFilterBackend
from .models import CampEnum, CampLeader, Image, OrgLeader, Commissioner, CabinOfficer
from rest_framework.filters import BaseFilterBackend
from kalunwa.core.utils import get_value_by_label



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
        related name should be 'gallery_<content>s' e.g. gallery_events
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
        if not limit.isdigit():
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


class CampNameInFilter(BaseFilterBackend):
    """
    used in camps endpoint
    expect a list of names here. (e.g. Suba,Lasang,)
    urls don't accept whitespaces, so don't have to worry bout that 
    spaces are automatically replaced with `%20`
    risky inputs
    #   Suba,,,,General,, -> would be accepted (same behavior for flex fields)
    returns empty list if name queried is invalid, and no other valid camp is queried
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


class OrgLeaderPositionFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        position = request.query_params.get('position', None)     
        if position is None:
            return queryset
        if position=="ExeComm":          
            execomm_leaders = queryset.exclude(              
            Q(position=OrgLeader.Positions.DIRECTOR.value) |
            Q(position=OrgLeader.Positions.OTHER.value)
            )
            return execomm_leaders
        position_value = get_value_by_label(position, OrgLeader.Positions)            
        if position_value is None: # invalid position (django-filter-like behavior)     
            return queryset.none()
        return queryset.filter(position=position_value)   

class CampLeaderPositionFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        position = request.query_params.get('position', None)     
        if position is None:
            return queryset
        position_value = get_value_by_label(position, CampLeader.Positions)            
        if position_value is None:    
            return queryset.none()
        return queryset.filter(position=position_value)   

class CampFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        camp = request.query_params.get('camp', None)                 
        if camp is None:
            return queryset
        camp_value = get_value_by_label(camp,CampEnum)            
        if camp_value is None:
            return queryset.none()   
        else:
            return queryset.filter(camp=camp_value)  


class CabinOfficerCategoryFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get('category', None)         
        if category is None:
            return queryset
        category_value = get_value_by_label(category, CabinOfficer.Categories)
        if category_value is None:
            return queryset.none()
        else:
            return queryset.filter(category=category_value)


class CommissionerCategoryFilter(BaseFilterBackend): 
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get('category', None)         
        if category is None:
            return queryset
        category_value = get_value_by_label(category, Commissioner.Categories)
        if category_value is None:
            return queryset.none()
        else:
            return queryset.filter(category=category_value)


class ExcludeIDFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        id = request.query_params.get('id__not', None)     
        if id is None or not id.isdigit():
            return queryset
        return queryset.exclude(id=int(id))    