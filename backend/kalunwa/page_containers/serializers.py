from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from kalunwa.content.models import Jumbotron
from kalunwa.content.serializers import JumbotronSerializer
from .models import PageContainer, PageContainedJumbotron
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class HomePageContainerSerializer(serializers.Serializer): # be used on different views 
    jumbotrons = JumbotronSerializer(many=True) 

    class Meta:
        fields = (
            'name',
            'jumbotrons',
            'created_at',
            'updated_at',
        )


# error
# if we were to post directly to featured jumbotrons 
class PageContainedJumbotronSerializer(serializers.ModelSerializer):
    # jumbotron = JumbotronSerializer() # change to get related_ID
    # container = PageContainerSerializer() # change to get related_ID
    class Meta:
        model = PageContainedJumbotron
        fields = (
            # 'container', #tried to get value for field`container`
            'id', # for some reason, it's not included
            'container',            
            'jumbotron',
            'section_order',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=PageContainedJumbotron.objects.all(),
                fields=["container", "jumbotron", "section_order"],
            ),
            UniqueTogetherValidator(
                queryset=PageContainedJumbotron.objects.all(),
                fields=["container", "section_order"],
            ),            
            UniqueTogetherValidator(
                queryset=PageContainedJumbotron.objects.all(),
                fields=["container", "jumbotron"],
            )                        
        ]           

class PageContainerSerializer(serializers.ModelSerializer):
    page_contained_jumbotrons = PageContainedJumbotronSerializer(
        source='pagecontainedjumbotron_set', many=True, required=False)

    class Meta:
        model = PageContainer
        fields = (
            'id',
            'name',
            'slug',
            'page_contained_jumbotrons',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'slug',
            'created_at',
            'updated_at',            
        )
        lookup_field = 'slug'

     
    
    # validate if jumbotron -> less than or equal to 5 entries
    # validate uniqueness 
    #   -> container & section order
    #   -> container & jumbotron

    def create_or_update_contained_jumbotrons(self, instance, contained_jumbotrons:dict)-> list: # get or create page_contained_jumbotrons
        contained_jumbotron_objects = []       
        for contained_jumbotron in contained_jumbotrons:
            try: 
                contained_jumbotron_obj = PageContainedJumbotron.objects.get(
                    container=instance,
                    section_order=contained_jumbotron['section_order']
                )
                contained_jumbotron_obj.jumbotron = contained_jumbotron['jumbotron']

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

    def update(self, instance, validated_data):
        # validated_data here needs to refer to db source (pagecontainedjumbotron_set)
        contained_jumbotrons = validated_data.pop('pagecontainedjumbotron_set', [])  
        instance.pagecontainedjumbotron_set.set(self.create_or_update_contained_jumbotrons(instance, contained_jumbotrons)) # get jumbotron by id 
        fields = ['name'] # direct fields in a container that can be updated 
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass        
        instance.save()

        return instance
