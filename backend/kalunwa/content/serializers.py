from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers
from rest_framework import validators as drf_validators
from rest_flex_fields.serializers import FlexFieldsModelSerializer, FlexFieldsSerializerMixin
from .models import Contributor, Image, Jumbotron, Tag, Announcement, Event, Project, News 
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from enum import Enum
from .validators import validate_start_date_and_end_date
from kalunwa.core.utils import to_formal_mdy


class StatusEnum(Enum):
    PAST = 'Past'
    ONGOING = 'Ongoing'
    UPCOMING = 'Upcoming'


class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        validators=[
            drf_validators.UniqueValidator(
                queryset=Tag.objects.all(),
                message="A tag name should be unique."
                )]
    )

    class Meta: # add tag ordering by name
        model = Tag
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            )


class ImageSerializer(FlexFieldsModelSerializer):
    image = serializers.ImageField(use_url=True)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'image',
            'tags',
            'created_at',
            'updated_at',
        )

        expandable_fields = {
            'events' : ('kalunwa.content.EventSerializer', {'many': True, 'source': 'gallery_events','fields':['id','title']}),
            'projects' : ('kalunwa.content.ProjectSerializer', {'many': True, 'source': 'gallery_projects','fields':['id','title']}),
            'camps' : ('kalunwa.content.CampPageSerializer', {'many': True, 'source': 'gallery_camps','fields':['id','name']}),
        }

class JumbotronSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'subtitle',
            'image',
            'created_at',
            'updated_at',
        )    

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        }


class OccurenceSerializer(FlexFieldsSerializerMixin, serializers.Serializer):
    """
    Inherited by project and event serializers given similar logic
    """
    # might just return dates in datetime format. reasons:
        # methods are view onlies, so client can't make records with start_date
            # and end_date (work around would involve making another serializer)
        # might be more appropriate to do display manipulations at the frontend
    # alternative: another field for datetime (for post/create) and display (get/list)? 
    status = serializers.SerializerMethodField()
    camp = serializers.CharField(source='get_camp')

    class Meta:
        fields = (
            'id',
            'title',
            'image',  # expose image pk or hide, then only access in expand?
            'description',
            'start_date',
            'end_date',            
            'camp', # choices serializer            
            'created_at',
            'updated_at',  
            'status',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),

            'gallery' : ('kalunwa.content.ImageSerializer',
                {
                 'many': True,
                 'fields':['id','image']
                 }            
            ),
            
            'contributors' : ('kalunwa.content.ContributorSerializer',
                {
                 'many': True,
                 }                  
            )               

        }

    def validate(self, data): # object-level validation
        data = self.get_initial() # gets pre-validation data
        validate_start_date_and_end_date(data['start_date'], data['end_date'])
        return data

    def determine_status(self, obj):
        date_now = timezone.now()
        if date_now > obj.start_date and date_now > obj.end_date:
            return StatusEnum.PAST.value 
        # ongoing
        if date_now >= obj.start_date and date_now < obj.end_date:
            return StatusEnum.ONGOING.value             
        # upcoming
        if date_now < obj.start_date and date_now < obj.end_date:
            return StatusEnum.UPCOMING.value   
        

class EventSerializer(OccurenceSerializer, serializers.ModelSerializer):

    class Meta(OccurenceSerializer.Meta):
        model = Event

    def get_status(self, obj)->str:
        return self.determine_status(obj)
           

class ProjectSerializer(OccurenceSerializer, serializers.ModelSerializer):

    class Meta(OccurenceSerializer.Meta):
        model = Project

    def get_status(self, obj)->str:
        if not obj.end_date: # if end_date does not exist
            return StatusEnum.ONGOING.value
        return self.determine_status(obj)       


class NewsSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'image',
            'created_at',
            'updated_at',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        }        

# prep for about us 
# will have separate serializer when posting 
    # position, camp, and name fields cannot be posted given the use of get_methods
    # unless the to_internal value is changed
class CampLeaderSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    position = serializers.CharField(source='get_position')
    camp = serializers.CharField(source='get_camp')   
    name = serializers.CharField(source='get_fullname')

    class Meta:
        model = CampLeader
        fields = (
            'id',
            'camp',
            'position',
            'name',
            'first_name',
            'last_name',
            'quote',
            'image',
            'motto', 
            'created_at',
            'updated_at',
        )    

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        }           

# will have separate serializer when posting 
    # name cannot be posted given the use of a get method
    # unless the to_internal value is changed
class CampPageSerializer(FlexFieldsModelSerializer):
    name = serializers.CharField(source='get_name') # behavior for creating data
    camp_leader = serializers.SerializerMethodField()

    class Meta:
        model = CampPage
        fields = (
            'id',
            'name',
            'description',
            'tagline',
            'image',
            'camp_leader',
            'created_at',
            'updated_at',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
            'gallery' : ('kalunwa.content.ImageSerializer',
                {
                 'many': True,
                 'fields':['id','image']
                 }            
            ),            
        }   

    def get_camp_leader(self, obj): # can't select fields if not related object (e.g. fk or m2m)
        try: # what if 2 leaders would be returned
            camp_leader = CampLeader.objects.get(
                camp=obj.name,
                position=CampLeader.Positions.LEADER
            ) 

            serializer = CampLeaderSerializer(
                camp_leader,
                context=self.context,
                fields = ['id', 'name', 'motto']
                )
            return serializer.data

        except ObjectDoesNotExist:
            return None


# will have separate serializer when posting 
    # position cannot be posted given the use of a get method
    # unless the to_internal value is changed
class OrgLeaderSerializer(FlexFieldsModelSerializer):
    position = serializers.CharField(source='get_position')

    class Meta:
        model = OrgLeader
        fields = (
            'id',
            'position',
            'first_name',
            'last_name',
            'quote',
            'image',
            'created_at',
            'updated_at',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 


# will have separate serializer when posting 
    # category cannot be posted given the use of a get method
    # unless the to_internal value is changed
class ContributorSerializer(FlexFieldsModelSerializer):
    category = serializers.CharField(source='get_category') 

    class Meta:
        model = Contributor
        fields = (
            'id',
            'name',
            'image', 
            'category',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 


#-------------------------------------------------------------------------------
#  serializes all data fields


class AnnouncementSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            'id',
            'title',
            'meta_description',
            'description',
            'created_at',
            'updated_at',
        )


class DemographicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demographics
        fields = (
            'id',
            'location',
            'member_count',
            'created_at',
            'updated_at',
        )

# will have separate serializer when posting 
    # position & category cannot be posted given the use of a get method
    # unless the to_internal value is changed
class CommissionerSerializer(FlexFieldsModelSerializer):
    position = serializers.CharField(source='get_position')
    category = serializers.CharField(source='get_category')

    class Meta:
        model = Commissioner
        fields = (
            'id',
            'category',
            'position',
            'first_name',
            'last_name',
            'quote',
            'image',
            'created_at',
            'updated_at',
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 


# will have separate serializer when posting 
    # position & category cannot be posted given the use of a get method
    # unless the to_internal value is changed
class CabinOfficerSerializer(FlexFieldsModelSerializer):
    position = serializers.CharField(source='get_position')
    camp = serializers.CharField(source='get_camp')
    category = serializers.CharField(source='get_category')

    class Meta:
        model = CabinOfficer
        fields = (
            'id',
            'category',
            'position',
            'first_name',
            'last_name',
            'quote',
            'image',
            'camp',
            'created_at',
            'updated_at',
        )
        
        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 

