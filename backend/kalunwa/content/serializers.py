from django.utils import timezone
from rest_framework import serializers
from rest_framework import validators as drf_validators
from .models import Image, Jumbotron, Tag, Announcement, Event, Project, News 
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from enum import Enum
from .validators import validate_start_date_and_end_date


class StatusEnum(Enum):
    PAST = 'past'
    ONGOING = 'ongoing'
    UPCOMING = 'upcoming'


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


class ImageURLSerializer(serializers.Serializer):
    """
    This serializer gets the absolute url of images, and returns
    only that field.
     Will be recycled for all serializers that will only require
    the complete url (exclude extra image data e.g. title, tags).
    note: 
    Serializer Models that will inherit this should have their models 
    use `image` as the field name.
    """
    url = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'url'
        )
    
    def get_url(self, obj):
        # get Image attribute from the object (e.g. jumbotron, event)
        image = Image.objects.get(pk=obj.image.pk)
        # pass context needed to generate full URL
        serializer = ImageSerializer(image, context=self.context)
        # serializer.data -> returns key dictionary pairs
        # accessing the 'image' key to get value (URL)
        return serializer.data['image']        


class ImageSerializer(serializers.ModelSerializer):
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

#-------------------------------------------------------------------------------
#  serializers for website homepage view

class HomepageJumbotronSerializer(serializers.ModelSerializer, ImageURLSerializer):
    image = serializers.SerializerMethodField(method_name='get_url')
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'subtitle',
            'image',         
        )


class HomepageEventSerializer(serializers.ModelSerializer, ImageURLSerializer):
    image = serializers.SerializerMethodField(method_name='get_url')
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'image'
        )


class HomepageProjectSerializer(serializers.ModelSerializer, ImageURLSerializer):
    image = serializers.SerializerMethodField(method_name='get_url')
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'image'
        )
    

class HomepageNewsSerializer(serializers.ModelSerializer, ImageURLSerializer):
    image = serializers.SerializerMethodField(method_name='get_url')
    date = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'date',
            'image'
        )
    
    def get_date(self, obj):
        return obj.homepage_date()


#-------------------------------------------------------------------------------
#  serializers for aboutus homepage view



#-------------------------------------------------------------------------------
#  serializes all data fields

class JumbotronSerializer(serializers.ModelSerializer):
    image = ImageSerializer() # or make it return the image resource
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


class EventSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'image',
            'start_date',
            'end_date',            
            'camp', # choices serializer            
            'created_at',
            'updated_at',  
            'status',
        )

    def get_status(self, obj)->str:
        # add check if no dates
        # past
        date_now = timezone.now()
        if date_now > obj.start_date and date_now > obj.end_date:
            return StatusEnum.PAST.value 
        # ongoing
        if date_now >= obj.start_date and date_now < obj.end_date:
            return StatusEnum.ONGOING.value             
        # upcoming
        if date_now < obj.start_date and date_now < obj.end_date:
            return StatusEnum.UPCOMING.value    
    
    def validate(self, data): # object-level validation
        data = self.get_initial() # gets pre-validation data
        start_date = data['start_date']
        end_date = data['end_date']
        validate_start_date_and_end_date(start_date, end_date)

        return data


class ProjectSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'image',
            'start_date',
            'end_date',            
            'camp',         
            'created_at',
            'updated_at',  
            'status',
        )
    def get_status(self, obj)->str:
        if not obj.end_date: # if end_date does not exist
            return StatusEnum.ONGOING.value

        date_now = timezone.now()
        if date_now > obj.start_date and date_now > obj.end_date:
            return StatusEnum.PAST.value 
        # ongoing
        if date_now >= obj.start_date and date_now < obj.end_date:
            return StatusEnum.ONGOING.value             
        # upcoming
        if date_now < obj.start_date and date_now < obj.end_date:
            return StatusEnum.UPCOMING.value    

    def validate(self, data): # object-level validation
        data = self.get_initial() # gets unvalidated data being posted
        start_date = data['start_date']
        end_date = data['end_date']
        validate_start_date_and_end_date(start_date, end_date)

        return data

class NewsSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
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


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = (
            'id',
            'title',
            'description',
            'created_at',
            'updated_at',
        )


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-----------------------------newly added serializer as of 23/3/2022-----------------------------------------------

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


class CampPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampPage
        fields = (
            'id',
            'name',
            'description',
            'image',
            'created_at',
            'updated_at',
        )


class OrgLeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgLeader
        fields = (
            'id',
            'first_name',
            'last_name',
            'background',
            'advocacy',
            'image',
            'position',
            'created_at',
            'updated_at',
        )


class CommissionerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commissioner
        fields = (
            'id',
            'first_name',
            'last_name',
            'background',
            'advocacy',
            'image',
            'position',
            'category',
            'created_at',
            'updated_at',
        )


class CampLeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampLeader
        fields = (
            'id',
            'first_name',
            'last_name',
            'background',
            'advocacy',
            'image',
            'camp',
            'position',
            'motto',
            'created_at',
            'updated_at',
        )

class CabinOfficerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CabinOfficer
        fields = (
            'id',
            'first_name',
            'last_name',
            'background',
            'advocacy',
            'image',
            'camp',
            'position',
            'category',
            'created_at',
            'updated_at',
        )
