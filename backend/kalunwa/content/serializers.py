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

