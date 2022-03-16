from datetime import datetime
from django.utils import timezone
from rest_framework import serializers
from .models import Image, Jumbotron, Tag, Announcement, Event


class TagSerializer(serializers.ModelSerializer):

    class Meta: # add tag ordering by name
        model = Tag
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            )
       

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


class HomepageJumbotronSerializer(serializers.ModelSerializer):
    featured_image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'featured_image',
            'short_description',            
            'featured_image'
        )

    def get_featured_image(self, obj): 
        # extra and experimental implementation in extracting full img URL
        #obj -> actual jumbotron object; can access model fields
        # serializer.data -> returns key dictionary pairs
        image = Image.objects.get(pk=obj.pk)
        serializer = ImageSerializer(image, context=self.context)
        return serializer.data['image'] # accessing the key to get value


#-------------------------------------------------------------------------------
#  serializes all data fields

class JumbotronSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer() # or make it return the image resource
    class Meta:
        model = Jumbotron
        fields = (
            'id',
            'header_title',
            'featured_image',
            'short_description',
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

class EventSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'featured_image',
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
            return 'past' 
        # ongoing
            # now_date >= start_date && now_date < end_date
        if date_now >= obj.start_date and date_now < obj.end_date:
            return 'ongoing'             
        # upcoming
            # now_date < start_date && now_date < end_date
        if date_now < obj.start_date and date_now < obj.end_date:
            return 'upcoming'    

