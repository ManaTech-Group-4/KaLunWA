from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS, # http methods -> get, head, options
)


class DefaultObjectPermission(BasePermission):
    """
    To watch out for when using bit OR in views:
        https://github.com/encode/django-rest-framework/issues/7117
    override default has_object_permission from:
            return True
        to ->
            return has_permission(...)
    """    
    def has_object_permission(self, request, view, obj): # pass -> false
        return self.has_permission(request, view)    


class SuperUserOnly(DefaultObjectPermission):
    """
    Superusers are the only one allowed to access the views with this permission.
    Must be superuser as well to be granted object permissions. 
    """
    def has_permission(self, request, view):
        """
        only superusers can access the endpoint. 
        """           
        return request.user.is_superuser


class AuthenticatedAndReadOnly(DefaultObjectPermission):
    """
    Only Authenticated users are allowed on endpoints, though they have limitations.
    They can only use safe methods: 
        GET, OPTIONS, HEAD
    """    
    def has_permission(self, request, view): 
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        return False

class SelfUserOnly(DefaultObjectPermission):
    """
    Only respective users can edit their user/account info.
    Note:
        - This is different to ownerCanEditDeleteOnly, as the latter refers
        to views wherein the objects/records involved are being owned by the user. 
    """
    def has_object_permission(self, request, view, obj):                              
        # Owners and superusers can update and delete themselves            
        if request.user.id == obj.id:
            return True
        return False      


class OwnersOnly(DefaultObjectPermission):
    """
    Only user owners of a record can edit/delete what ever they owned. 
    """
    def has_object_permission(self, request, view, obj):
        # Owners and superusers can update and delete themselves            
        if request.user == obj.user:
            return True
        return False    



########################################## not used 
class IsProfileOwnerOrReadOnlyAdmin(BasePermission):
    """
    - User owning the profile can read and edit
    - Other admins can only read (is_authenticated)
    to be put on:
        - UserProfileList
            - all authenticated users can view
            - only superusers can create
        - UserProfileDetail
            - all authenticated users can view
            - only owners can edit 
    """
    message = "Profile owner can read and edit, while other admins are limited"\
              " to viewing only."

    def has_permission(self, request, view): # for list
        """
        Profile details should not be viewed publicly. If they are authenticated,
        they can access list and detail views. 
        """
        # authenticated users can view other profiles (& other safe methods)        
        if not request.user.is_authenticated:
            return False
        # only super users can create
        if request.method == 'POST' and not request.user.is_superuser:
            return False
        return True 

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True            
        if request.method in SAFE_METHODS:
            return True       
        if request.method == 'DELETE': # profiles cannot be deleted via views
            return False             
        # only owners can update their own profiles
        return obj.owner == request.user 


class AdminAuthorPermission(BasePermission):
    """
    methods should return a boolean value (true or false)
    """
    message = 'Adding customers not allowed.'

    def has_permission(self, request, obj, view):
        """
        if is_authenticated and
        is_admin         # 
        | is_super_admin # add and delete 
        | is_super_user  # can do anything
        """
        pass


    def has_object_permission(self, request, view, obj):
        pass


class SuperAdminAuthorPermission(BasePermission):
    pass

# check the roles before doing an action?
# using these because we can attach them to classes .. and are much cleaner

# # is admin
#     # has object permissions for:
#     # - profile
#         - edit, update
#     # add, edit, update, delete:
#         - events 
#         - projects
#         - news
#         - announcements
#         - jumbotrons
#         - org_leaders
#         - image
#         - demographics
#         - contributor 
#     # edit, update
#         - camppage 

# # is superadmin
#     # has add and delete permissions:
#         - profile and user