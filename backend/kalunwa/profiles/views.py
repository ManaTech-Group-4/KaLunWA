from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView

)
from kalunwa.profiles.models import Profile
from kalunwa.profiles.serializers import ProfileSerializer


class ProfileListView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(RetrieveUpdateAPIView):
    """
    Only image can be updated as of the moment, as the handling of form data 
    is done separately. Parsing Json data and form data is a bit complex so the 
    combo is not included/implemented.
    . Other profile data should be changed on the user info endpoint. 
    Test:
        - patch -> image only
    
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()