from rest_framework import serializers
from .models import Image, Tag


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

