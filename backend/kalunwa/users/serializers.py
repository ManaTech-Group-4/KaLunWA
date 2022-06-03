from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Override to put additional info on the token's payload (e.g. email). 
    """
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        # will be changed to first & last name when user profile is set up 
          # token['username']
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data): 
        # what if password is none during posting 
            # -> caught by model serializer from abstract user -> field is required.
        # what if email is an invalid format 
            # -> is the check also covered by the serializer? -> invalid format
        # check for email duplicates when registering (registerView)
            # covered by model serializer -> email = field(unique=True)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # hash password here before saving to db
            instance.set_password(password)
        instance.save()
        return instance