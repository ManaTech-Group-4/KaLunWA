from django.urls import path
from .views import (
    BlacklistTokenUpdateView, 
    UserCreateView,
    UserRetrieveUpdateDestroyView,     
    UserListView
)


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('logout/blacklist/',
            BlacklistTokenUpdateView.as_view(),
            name='token-blacklist'),    
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('', UserListView.as_view(), name='user-list')    
]