from .views import (
    ProfileListView, 
    UserProfileDetailView, 
    UpdateProfilePhotoView,
)
from django.urls import path




urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='userprofile-list'),
    # used mainly to fetch all profiles. This can also be done in the user endpoint,
    # but as researched, the user serializer should not be revealing profile information.
    # Make it flexible: if the user is the profile owner, they can update their info. 
    # Though another endpoint (users/<pk>/profile) is provided to allow the frontend
    # to retrieve their profile using their ID.

    # updating images (form data) should be done separately to that of json data.
    # patch method should be used. 

    # id here is profile id
    # path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),    

    path('users/<int:pk>/profile/', UserProfileDetailView.as_view(), name='user-profile-detail'),     
    path('users/<int:pk>/profile/update-image/', UpdateProfilePhotoView.as_view(), name='update-profile-photo'),        
    
    # change file upload
    # id here is user id 

    # change user data
    # users/id
]


# users/<pk>/profile -> image_upload via formdata
# users/<pk>/ 
#   -> patch/update -> deets
#    -> change_password 
        # old_password
        # new_password
        # new_password_rewritten 
            # check if old password matches 
            # compare if both new_passwords are correct
            # if correct, update user password  