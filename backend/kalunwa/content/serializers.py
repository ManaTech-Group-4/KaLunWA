from rest_framework import serializers
from .models import Image, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta: # add tag ordering by name
        model = Tag
        fields = ('id','name',)
        


class ImageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, )

    class Meta:
        model = Image
        fields = ('id','title', 'image', 'tags',)