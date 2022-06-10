from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from kalunwa.content.models import Jumbotron
from kalunwa.content.serializers import JumbotronSerializer
from .models import (
    PageContainedProject,
    PageContainer, 
    PageContainedJumbotron,
    PageContainedEvent,
)

from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from rest_flex_fields.serializers import FlexFieldsModelSerializer, FlexFieldsSerializerMixin


class PageContainedJumbotronSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContainedJumbotron
        fields = (
            # 
            'id', 
            'container', #requiring this because of the unique validator check, but can be removed if validator is changed            
            'jumbotron',
            'section_order',
        )          


class PageContainedJumbotronReadSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PageContainedJumbotron
        fields = (
            # 
            'id', 
            'container', 
            'jumbotron',
            'section_order',
        )
        expandable_fields = {
            'jumbotron' : ('kalunwa.content.JumbotronSerializer')
        }        


class PageContainedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContainedEvent
        fields = (
            # 
            'id', 
            'container', 
            'event',
            'section_order',
        )          


class PageContainedEventReadSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PageContainedEvent
        fields = (
            # 
            'id', 
            'container', 
            'event',
            'section_order',
        )
        expandable_fields = {
            'event' : ('kalunwa.content.EventSerializer')
        } 


class PageContainedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContainedProject
        fields = (
            # 
            'id',
            'container', 
            'project',
            'section_order',
        )          


class PageContainedProjectReadSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PageContainedProject
        fields = (
            # 
            'id', 
            'container', 
            'project',
            'section_order',
        )
        expandable_fields = {
            'project' : ('kalunwa.content.ProjectSerializer')
        } 

class PageContainerReadSerializer(FlexFieldsModelSerializer):    
    """
    Many to many related records are made deferred fields. This means that 
    when accessing the base endpoint e.g. api/page-containers/homepage/,
    only the fields explicitly written on the fields under Meta are shown. 
    
    Deferred fields should be expanded for the data to be seen. 

    """
    class Meta:
        model = PageContainer
        fields = ( 
            'id',
            'name',
            'slug',          
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'slug',
            'created_at',
            'updated_at',            
        )
        lookup_field = 'slug'

        expandable_fields = {
            'page_contained_jumbotrons' : 
            (
                'kalunwa.page_containers.PageContainedJumbotronReadSerializer',
                {'many': True, 'source': 'pagecontainedjumbotron_set'}
            ),        
            'page_contained_events' : 
            (
                'kalunwa.page_containers.PageContainedEventReadSerializer',
                {'many': True, 'source': 'pagecontainedevent_set'}
            ),                   
            'page_contained_projects' : 
            (
                'kalunwa.page_containers.PageContainedProjectReadSerializer',
                {'many': True, 'source': 'pagecontainedproject_set'}
            ), 
        }


class PageContainerSerializer(serializers.ModelSerializer):
    page_contained_jumbotrons = PageContainedJumbotronSerializer(
        source='pagecontainedjumbotron_set', many=True, required=False)
    page_contained_events = PageContainedEventSerializer(
        source='pagecontainedevent_set', many=True, required=False)
    page_contained_projects = PageContainedProjectSerializer(
        source='pagecontainedproject_set', many=True, required=False)        

    class Meta:
        model = PageContainer
        fields = (
            'id',
            'name',
            'slug',
            'page_contained_jumbotrons',
            'page_contained_events',
            'page_contained_projects',            
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'slug',
            'created_at',
            'updated_at',            
        )
        lookup_field = 'slug'

    def create_or_update_contained_jumbotrons(self, instance, contained_jumbotrons:dict)-> list: # get or create page_contained_jumbotrons
        contained_jumbotron_objects = []       
        for contained_jumbotron in contained_jumbotrons:
            try: 
                contained_jumbotron_obj = PageContainedJumbotron.objects.get(
                    container=instance,
                    section_order=contained_jumbotron['section_order']
                )
                contained_jumbotron_obj.jumbotron = contained_jumbotron['jumbotron']
                contained_jumbotron_obj.save()

            except ObjectDoesNotExist:
                if instance.name == 'homepage' and PageContainedJumbotron.objects.count() == 5:
                    raise serializers.ValidationError({"detail": "Homepage can only contain 5 jumbotrons at most."})

                contained_jumbotron_obj = PageContainedJumbotron.objects.create(
                    container=instance,
                    section_order=contained_jumbotron['section_order'],
                    jumbotron=contained_jumbotron['jumbotron']
                )
            
            contained_jumbotron_objects.append(contained_jumbotron_obj)

        return contained_jumbotron_objects

    def create_or_update_contained_events(self, instance, contained_events:dict)-> list: # get or create page_contained_jumbotrons
        contained_event_objects = []       
        for contained_event in contained_events:
            try: 
                contained_event_obj = PageContainedEvent.objects.get(
                    container=instance,
                    section_order=contained_event['section_order']
                )
                contained_event_obj.event = contained_event['event']
                contained_event_obj.save()

            except ObjectDoesNotExist:
                if instance.name == 'homepage' and PageContainedEvent.objects.count() == 3:
                    raise serializers.ValidationError({"detail": "Homepage can only contain 3 events at most."})

                contained_event_obj = PageContainedEvent.objects.create(
                    container=instance,
                    section_order=contained_event['section_order'],
                    event=contained_event['event']
                )
            contained_event_objects.append(contained_event_obj)

        return contained_event_objects

    def create_or_update_contained_projects(self, instance, contained_projects:dict)-> list: # get or create page_contained_jumbotrons
        contained_project_objects = []       
        for contained_project in contained_projects:
            try: 
                contained_project_obj = PageContainedProject.objects.get(
                    container=instance,
                    section_order=contained_project['section_order']
                )
                contained_project_obj.project = contained_project['project']
                contained_project_obj.save()

            except ObjectDoesNotExist:
                if instance.name == 'homepage' and PageContainedProject.objects.count() == 3:
                    raise serializers.ValidationError({"detail": "Homepage can only contain 3 projects at most."})

                contained_project_obj = PageContainedProject.objects.create(
                    container=instance,
                    section_order=contained_project['section_order'],
                    project=contained_project['project']
                )
            contained_project_objects.append(contained_project_obj)

        return contained_project_objects

    def update(self, instance, validated_data):
        # validated_data here needs to refer to the model's manytomany referral source (pagecontainedjumbotron_set)
        contained_jumbotrons = validated_data.pop('pagecontainedjumbotron_set', [])  
        contained_events = validated_data.pop('pagecontainedevent_set', [])   
        contained_projects = validated_data.pop('pagecontainedproject_set', [])       
        instance.pagecontainedjumbotron_set.add(*self.create_or_update_contained_jumbotrons(instance, contained_jumbotrons)) 
        instance.pagecontainedevent_set.add(*self.create_or_update_contained_events(instance, contained_events))         
        instance.pagecontainedproject_set.add(*self.create_or_update_contained_projects(instance, contained_projects))
        fields = ['name'] # direct fields in a container that can be updated 
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass        
        instance.save()
        return instance
