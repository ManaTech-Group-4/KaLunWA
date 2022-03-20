from django.utils import timezone
from rest_framework import serializers
from .models import Image, Jumbotron, Tag, Announcement, Event, Project, News
from enum import Enum

class StatusEnum(Enum):
    PAST = 'past'
    ONGOING = 'ongoing'
    UPCOMING = 'upcoming'


class TagSerializer(serializers.ModelSerializer):

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
    tags = TagSerializer(many=True, required=False)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = (
            'id',
            'title',
            'image',
            'tags',
            'created_at',
            'updated_at',
        )

#-------------------------------------------------------------------------------
#  serializes needed fields for website homepage view

class HomepageJumbotronSerializer(serializers.ModelSerializer, ImageURLSerializer):
    image = serializers.SerializerMethodField(method_name='get_url')
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'image',
            'short_description',            
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
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'image'
        )


serializers.ImageField(use_url=True)
#-------------------------------------------------------------------------------
#  serializes all data fields

class JumbotronSerializer(serializers.ModelSerializer):
    image = ImageSerializer() # or make it return the image resource
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'image',
            'short_description',
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
            # now_date > start_date && now_date > end date 
        date_now = timezone.now()
        if date_now > obj.start_date and date_now > obj.end_date:
            return StatusEnum.PAST.value 
        # ongoing
            # now_date >= start_date && now_date < end_date
        if date_now >= obj.start_date and date_now < obj.end_date:
            return StatusEnum.ONGOING.value             
        # upcoming
            # now_date < start_date && now_date < end_date
        if date_now < obj.start_date and date_now < obj.end_date:
            return StatusEnum.UPCOMING.value    


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


class NewsSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'description',
            'featured_image',
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
