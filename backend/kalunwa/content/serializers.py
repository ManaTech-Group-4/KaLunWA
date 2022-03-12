from rest_framework import serializers
from .models import Image, Jumbotron, Tag


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

