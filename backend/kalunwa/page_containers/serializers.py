from kalunwa.content.serializers import JumbotronSerializer
from .models import PageContainer, PageContainedJumbotron

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
            'jumbotron',
            'section_order',
        )

class PageContainerSerializer(serializers.ModelSerializer):
    jumbotrons = PageContainedJumbotronSerializer(
        source='pagecontainedjumbotron_set', many=True, required=False)

    class Meta:
        model = PageContainer
        fields = (
            'id',
            'name',
            'slug',
            'jumbotrons',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'slug',
            'created_at',
            'updated_at',            
        )
        lookup_field = 'slug'


    # def create(self, validated_data):
    #     # will not create related objects
    #     # pop out related objects
    #     jumbotrons = validated_data.pop('jumbotrons', [])
    #         # check if related obj does not exist (exists):
    #             # raise error
    #         # create page container, 
    #             # then link it to the ...set() -> obj.jumbotrons.set() -> or sumth like that
    #     # return page

        # return super().create(validated_data)

