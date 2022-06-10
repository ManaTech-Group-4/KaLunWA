import profile
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
     IsAuthenticated, 
)
from kalunwa.users.permissions import (
    AuthenticatedAndReadOnly,
    OwnersOnly,
    SuperUserOnly,
)
from kalunwa.profiles.models import Profile
from kalunwa.profiles.serializers import ProfileSerializer, UploadProfilePhotoSerializer
from kalunwa.users.models import User
from kalunwa.profiles.models import Profile
from kalunwa.profiles.serializers import ProfileSerializer


class ProfileListView(ListAPIView):
    permission_classes = [
        IsAuthenticated # all authenticated users can view the profile (admin) list. 
        ]    
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


# class ProfileDetailView(RetrieveUpdateAPIView): 
#     # show all admin profile info
#         # if user clicks admin info, 
#           # -> redirect to api/users/user_pk/profile
#           # -> instead of api/profiles/<profile:pk>
#           # this view should be taken down
#     """
#     Only image can be updated as of the moment, as the handling of form data 
#     is done separately. Parsing Json data and form data is a bit complex so the 
#     combo is not included/implemented.
#     . Other profile data should be changed on the user info endpoint. 
#     Test:
#         - patch -> image only
    
#     """
#     permission_classes = [
#         SuperUserOnly | # super users can edit (?) given their nature.
#         OwnersOnly | # aside from super users, owner of the profile can edit
#         AuthenticatedAndReadOnly # Authenticated users can only view the detail.
#         ]
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()

    
class UserProfileDetailView(RetrieveUpdateAPIView): 
    """
    Access profile using user ID. Endpoint used for updating image.
    endpoint:
        /api/users/<pk>/profile/
    """
    permission_classes = [
        SuperUserOnly |
        OwnersOnly |
        AuthenticatedAndReadOnly
    ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self, **kwargs):
        user_id = self.kwargs['pk']
        profile = get_object_or_404(Profile, user__pk=user_id)
        return profile


class UpdateProfilePhotoView(APIView):
    """
    permissions for API view
    """
    def get_object(self, user_pk):
        profile = get_object_or_404(Profile, user__pk=user_pk)
        return profile

    def put(self, request, user_pk):
        profile = self.get_object(user_pk)
        serializer = UploadProfilePhotoSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data="Photo update successful.", status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)