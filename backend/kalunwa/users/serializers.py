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
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_superadmin'] = user.is_superuser
        token['image'] = user.image.name
        return token


class UserSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    - Used for viewing and updating (except password)
    
    -> UserRetrieveUpdateDestroy 
    
    """
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    username = serializers.CharField(max_length=255, required=False, allow_blank=True)
    image = serializers.ImageField(allow_empty_file=True, allow_null=True, required=False, use_url=True)
    is_superadmin = serializers.BooleanField(source='is_superuser', read_only=True)
    date_added = serializers.CharField(source="created_at", read_only=True) 
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    class Meta: 
        model = User 
        fields = [
            'id', 
            'first_name',
            'last_name',
            'image', 
            'username',
            'email',
            'is_superadmin',
            'date_added'
            ]


class UserRegisterSerializer(serializers.ModelSerializer):
    """
     Use in UserCreateView
    """
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    username = serializers.CharField(max_length=255, required=False, allow_blank=True)
    image = serializers.ImageField(required=False, allow_empty_file=True, allow_null=True,)    
    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )         
    date_added = serializers.CharField(source="created_at", read_only=True)     

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'image',
            'email',
            'password',
            'date_added',            
            ]    
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


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )     
    new_password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )      
    class Meta:
        fields = [
        'password',     
        'new_password',  
        ]

    def update(self, instance, validated_data):
        """
        Check if password matches the request maker's password.
         - hash password, compare if equal to instance.password.
        Will have to unhash the password stored in the database. 
        """
        password = validated_data.pop('password')
        if not instance.check_password(password):
            raise serializers.ValidationError(detail="Password incorrect.", code='invalid')
        
        new_password = validated_data.pop('new_password')
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance