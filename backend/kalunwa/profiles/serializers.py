# User is created in a different endpoint
    # api/users/
    # their profile is automatically created by a post signal
    # User info
        # email
        # password
# To update 
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from kalunwa.users.serializers import UserSerializer
from .models import Profile
from kalunwa.users.models import User

class ProfileSerializer(serializers.ModelSerializer):
    """
    Can be used to update user info, but must override update function
    """
    user = UserSerializer()
    image = serializers.ImageField(use_url=True, read_only=True)
    role = serializers.CharField(source='get_role', read_only=True)

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'image',
            'role',
            'created_at',
            'updated_at',            
        )

    def update(self, instance, validated_data):
        user_id = instance.user.id
        user_data = validated_data.pop('user', None)
        # get fields
        first_name = user_data.get('first_name', None)
        last_name = user_data.get('last_name', None)
        username = user_data.get('username', None)
        email = user_data.get('email', None)

        user = get_object_or_404(User, pk=user_id)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name         
        if username:
            user.username = username      
        if email:
            user.email = email                              

        user.save()
               
        return user.profile

class UploadProfilePhotoSerializer(serializers.Serializer):
    image = serializers.ImageField(write_only=True, allow_empty_file=True, allow_null=True, required=False)

    class Meta:
        fields = (
            'id',
            'image',
        )        
