from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers
from rest_framework import validators as drf_validators
from rest_flex_fields.serializers import FlexFieldsModelSerializer, FlexFieldsSerializerMixin
from .models import CampEnum, Contributor, Image, Jumbotron, Tag, Announcement, Event, Project, News 
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from enum import Enum
from .validators import validate_camp, validate_start_date_and_end_date
from kalunwa.core.utils import get_value_by_label, iso_to_datetime
from django.shortcuts import get_object_or_404

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
            'last_updated_by',                          
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
            'last_updated_by',             
        )    

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        }
        def create(self, validated_data):
            image_id = validated_data.pop('image')
            jumbotron_image = get_object_or_404(Image, pk=image_id)

            return Jumbotron.objects.create(
                image=jumbotron_image,
                **validated_data
            )

        def update(self, instance, validated_data):
            image_id = validated_data.pop('image')
            jumbotron_image = get_object_or_404(Image, pk=image_id)
            instance.image = jumbotron_image
            # update the rest of the attributes
            for key, value in validated_data.items():
                setattr(instance, key, value) 

            instance.save()        
            return instance


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
            'last_updated_by',              
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
        validate_camp(data['camp'])
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

    def create(self, validated_data):
        image_id = validated_data.pop('image')
        event_image = get_object_or_404(Image, pk=image_id)

        start_date = validated_data.pop('start_date')
        end_date = validated_data.pop('end_date')
        camp = validated_data.pop('camp')
        camp = get_value_by_label(camp, CampEnum)

        return Event.objects.create(
            image=event_image,
            start_date=iso_to_datetime(start_date),
            end_date=iso_to_datetime(end_date),
            camp=camp,
            **validated_data
        )

    def update(self, instance, validated_data):
        # pop stuff that needs to be processed
        image_id = validated_data.pop('image')
        event_image = get_object_or_404(Image, pk=image_id)
        instance.image = event_image
        camp = validated_data.pop('camp')
        camp = get_value_by_label(camp, CampEnum)
        instance.camp = camp

        # process datetime to iso format
        start_date = validated_data.pop('start_date')
        instance.start_date = iso_to_datetime(start_date)
        end_date = validated_data.pop('end_date')        
        instance.end_date = iso_to_datetime(end_date)

        # update the rest of the attributes
        for key, value in validated_data.items():
        # setattr updates an instance's attribute (key) with the value
            setattr(instance, key, value) 
        # always do instance.save() when editing an attribute, because assignment
        # itself does not commit to the database 
        instance.save()
        return instance
           

class ProjectSerializer(OccurenceSerializer, serializers.ModelSerializer):
    
    class Meta(OccurenceSerializer.Meta):
        model = Project

    def get_status(self, obj)->str:
        if not obj.end_date: # if end_date does not exist
            return StatusEnum.ONGOING.value
        return self.determine_status(obj)       
    
    def create(self, validated_data):
        image_id = validated_data.pop('image')
        event_image = get_object_or_404(Image, pk=image_id)

        start_date = validated_data.pop('start_date')
        end_date = validated_data.pop('end_date')
        camp = validated_data.pop('camp')

        return Project.objects.create(
            image=event_image,
            start_date=iso_to_datetime(start_date),
            end_date=iso_to_datetime(end_date),
            camp=camp,
            **validated_data
            )

    def update(self, instance, validated_data):
        image_id = validated_data.pop('image')
        project_image = get_object_or_404(Image, pk=image_id)
        instance.image = project_image
        camp = validated_data.pop('camp')
        camp = get_value_by_label(camp, CampEnum)
        instance.camp = camp

        start_date = validated_data.pop('start_date')
        instance.start_date = iso_to_datetime(start_date)
        end_date = validated_data.pop('end_date')        
        instance.end_date = iso_to_datetime(end_date)
        # update the rest of the attributes
        for key, value in validated_data.items():
            setattr(instance, key, value) 

        instance.save()        
        return instance

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
            'last_updated_by',             
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        }        

    # def create(self, validated_data):
    #     image_id = validated_data.pop('image')
    #     print(image_id)
    #     news_image = get_object_or_404(Image, pk=image_id)

    #     return News.objects.create(
    #         image=news_image,            
    #         **validated_data
    #         )

    def update(self, instance, validated_data):
        image_id = validated_data.pop('image')
        news_image = get_object_or_404(Image, pk=image_id)
        instance.image = news_image
        
        # update the rest of the attributes
        for key, value in validated_data.items():
            setattr(instance, key, value) 

        instance.save()          
        return instance

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
            'last_updated_by',             
        )
# if there's no fields to do extra processes to, create & update don't need to 
# be overwritten

# will have separate serializer when posting 
    # name cannot be posted given the use of a get method
    # unless the to_internal value is changed
class CampPageSerializer(FlexFieldsModelSerializer):
    # empty default validators to not force shortened version
    name = serializers.CharField(source='get_name', validators=[]) 
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
            'last_updated_by',             
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


    def validate(self, data): 
        validate_camp(data['name'])
        return data

    def create(self, validated_data):
        image_id = validated_data.pop('image')
        camp_image = get_object_or_404(Image, pk=image_id)
        
        name = validated_data.pop('name')
        camp_name = get_value_by_label(name, CampEnum)

        return CampPage.objects.create(
            image=camp_image,
            name=camp_name,
            **validated_data
        )

    def update(self, instance, validated_data):
        # pop stuff that needs to be processed
        image_id = validated_data.pop('image')
        camp_image = get_object_or_404(Image, pk=image_id)
        instance.image = camp_image
        
        camp = validated_data.pop('name')
        camp_name = get_value_by_label(camp, CampEnum)
        instance.name = camp_name

        # update the rest of the attributes
        for key, value in validated_data.items():
            setattr(instance, key, value) 
        instance.save()
        return instance


class ContributorSerializer(FlexFieldsModelSerializer):
    category = serializers.CharField(source='get_category', validators=[]) 

    class Meta:
        model = Contributor
        fields = (
            'id',
            'name',
            'image', 
            'category',
            'last_updated_by',             
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 

    def validate(self, data): 
        if data['category'] not in Contributor.Categories.labels:
            raise serializers.ValidationError("Contributor category is invalid.")
        return data

    def create(self, validated_data):
        image_id = validated_data.pop('image')
        contributor_image = get_object_or_404(Image, pk=image_id)

        category = validated_data.pop('category')
        category_value = get_value_by_label(category, Contributor.Categories)

        return Contributor.objects.create(
            image=contributor_image,
            category=category_value,
            **validated_data
        )

    def update(self, instance, validated_data):
        image_id = validated_data.pop('image')
        contributor_image = get_object_or_404(Image, pk=image_id)
        instance.image = contributor_image

        category = validated_data.pop('category')
        category_value = get_value_by_label(category, Contributor.Categories)
        instance.category = category_value

        for key, value in validated_data.items():
            setattr(instance, key, value) 

        instance.save()
        return instance

#-------------------------------------------------------------------------------
#  serializes all data fields

class DemographicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demographics
        fields = (
            'id',
            'location',
            'member_count',
            'created_at',
            'updated_at',
            'last_updated_by',                         
        )


class CommissionerSerializer(FlexFieldsModelSerializer):
    """
    Overriding to allow writes, though this gets rid of the custom validation
    as provided by django
    """
    position = serializers.CharField()
    category = serializers.CharField() 

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
            'last_updated_by',         
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 

    def validate(self, data):
        if data['category'] not in Commissioner.Categories.labels:
            raise serializers.ValidationError(
                f"Commissioner category invalid. Accepted are {Commissioner.Categories.labels}."
            )

        if data['position'] not in Commissioner.Positions.labels:
            raise serializers.ValidationError(
                f"Commissioner position invalid. Accepted are {Commissioner.Positions.labels}."
            )            
        return data

    def create(self, validated_data):
        category = validated_data.pop('category')
        category_value = get_value_by_label(category, Commissioner.Categories)
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, Commissioner.Positions)        

        return  Commissioner.objects.create(
            category=category_value,
            position=position_value,
            **validated_data)

    def update(self, instance, validated_data):
        category = validated_data.pop('category')
        category_value = get_value_by_label(category, Commissioner.Categories)
        instance.category = category_value

        position = validated_data.pop('position')
        position_value = get_value_by_label(position, Commissioner.Positions)        
        instance.position = position_value

        for key, value in validated_data.items():
            setattr(instance, key, value) 

        instance.save()
        return instance        

    def to_representation(self, instance):
        data = super(CommissionerSerializer, self).to_representation(instance)
        position = data.get('position', None) 
        category = data.get('category', None)        
        # when getting record, change presentation 
        if position is not None:
            data['position'] = instance.get_position() 
        if category is not None:
            data['category'] = instance.get_category()                          
        return data


# will have separate serializer when posting 
    # position & category cannot be posted given the use of a get method
    # unless the to_internal value is changed
class CabinOfficerSerializer(FlexFieldsModelSerializer):
    position = serializers.CharField(validators=[])
    camp = serializers.CharField(validators=[])
    category = serializers.CharField(validators=[]) 

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
            'last_updated_by',             
        )
        
        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 

    def validate(self, data): 
        validate_camp(data['camp'])

        if data['category'] not in CabinOfficer.Categories.labels:
            raise serializers.ValidationError(
                f"CabinOfficer category invalid. Accepted are {CabinOfficer.Categories.labels}"
            )

        if data['position'] not in CabinOfficer.Positions.labels:
            raise serializers.ValidationError(
                f"CabinOfficer position invalid. Accepted are {CabinOfficer.Positions.labels}"
            )
        return data
    
    def create(self, validated_data):      
        category = validated_data.pop('category')
        category_value = get_value_by_label(category, CabinOfficer.Categories)
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, CabinOfficer.Positions)        
        camp = validated_data.pop('camp')
        camp = get_value_by_label(camp, CampEnum)

        return  CabinOfficer.objects.create(
            category=category_value,
            position=position_value,
            camp=camp,
            **validated_data)

    def update(self, instance, validated_data):
        category = validated_data.pop('category')
        category_value = get_value_by_label(category, CabinOfficer.Categories)
        instance.category = category_value

        position = validated_data.pop('position')
        position_value = get_value_by_label(position, CabinOfficer.Positions)        
        instance.position = position_value
        
        for key, value in validated_data.items():
            setattr(instance, key, value) 

        instance.save()
        return instance 


    def to_representation(self, instance):
        data = super(CabinOfficerSerializer, self).to_representation(instance)
        position = data.get('position', None) 
        camp = data.get('camp', None) 
        category = data.get('category', None)        
        # when getting record, change presentation 
        if position is not None:
            data['position'] = instance.get_position()
        if camp is not None:
            data['camp'] = instance.get_camp()    
        if category is not None:
            data['category'] = instance.get_category()                          
        return data

# prep for about us 
class CampLeaderSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    position = serializers.CharField( validators=[])
    camp = serializers.CharField( validators=[])   
    name = serializers.CharField(source='get_fullname', read_only=True)

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
            'last_updated_by',             
        )    

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 

    def validate(self, data): 
        validate_camp(data['camp'])
        if data['position'] not in CampLeader.Positions.labels:
            raise serializers.ValidationError(
            f"Organization Leader position invalid. Expected are {CampLeader.Positions.labels}"
            )       
        return data

    def create(self, validated_data):
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, CampLeader.Positions)

        camp = validated_data.pop('camp')
        camp = get_value_by_label(camp, CampEnum)

        return  CampLeader.objects.create(
            position=position_value,
            camp=camp,
            **validated_data)

    def update(self, instance, validated_data):
        """
        Does not support patch, must have all fields
        """
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, CampLeader.Positions)
        instance.position = position_value

        camp = validated_data.pop('camp')
        camp_value = get_value_by_label(camp, CampEnum)
        instance.camp = camp_value   

        for key, value in validated_data.items():
                setattr(instance, key, value) 

        instance.save()        
        return instance

    def to_representation(self, instance):
        data = super(CampLeaderSerializer, self).to_representation(instance)
        position = data.get('position', None) 
        camp = data.get('camp', None) 
        # when getting record, change presentation 
        if position is not None:
            data['position'] = instance.get_position()
        if camp is not None:
            data['camp'] = instance.get_camp()            
        return data


class OrgLeaderSerializer(FlexFieldsModelSerializer):
    position = serializers.CharField(validators=[])
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
            'last_updated_by',             
        )

        expandable_fields = {
            'image' : ('kalunwa.content.ImageSerializer', 
                {
                 'fields':['id','image']
                }
            ),
        } 
    def validate(self, data): # object-level validation
        if data['position'] not in OrgLeader.Positions.labels:
            raise serializers.ValidationError(
            f"Organization Leader position invalid. Expected are {OrgLeader.Positions.labels}"
            )            
        return data

    def create(self, validated_data):
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, OrgLeader.Positions)
        return  OrgLeader.objects.create(
            position=position_value,
            **validated_data)

    def update(self, instance, validated_data):
        position = validated_data.pop('position')
        position_value = get_value_by_label(position, OrgLeader.Positions )
        instance.position = position_value

        for key, value in validated_data.items():
            setattr(instance, key, value) 
        instance.save()        
        return instance        

    def to_representation(self, instance):
        data = super(OrgLeaderSerializer, self).to_representation(instance)
        position = data.get('position', None) 
        # when getting record, change presentation 
        if position is not None:
            data['position'] = instance.get_position()
        return data