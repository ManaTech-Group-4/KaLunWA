from django.urls import path
from .views import (
    BlacklistTokenUpdateView,
    UserChangePasswordView, 
    UserCreateView,
    UserRetrieveUpdateDestroyView,     
    UserListView,
)


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('logout/blacklist/',
            BlacklistTokenUpdateView.as_view(),
            name='token-blacklist'),    
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('<int:pk>/change-password/', UserChangePasswordView.as_view(), name='user-change-password'),        
    path('', UserListView.as_view(), name='user-list'),
    # returns about the same view as `profiles/<profile:pk>/`, though it's difference
    # is that this endpoint shows their relationship to a user, making it easier
    # to access when given the user id upon the admin's login
]