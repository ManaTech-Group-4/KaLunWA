# User is created in a different endpoint
    # api/users/
    # their profile is automatically created by a post signal
    # User info
        # email
        # password
# To update 
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers
from kalunwa.users.serializers import UserSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = serializers.ImageField(use_url=True)
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
