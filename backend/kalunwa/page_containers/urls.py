from django.urls import path, include
from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    PageContainedProjectDetailView,
    PageContainerListView,
    PageContainerDetailView,
    PageContainedJumbotronDetailView,
    PageContainedEventDetailView
)

urlpatterns = [
    path('page-containers/', PageContainerListView.as_view(), name='page-container-list'),
    path('page-containers/<int:pk>/', PageContainerDetailView.as_view(), name='page-container-detail'),    
    path('page-containers/<slug:slug>/', PageContainerDetailView.as_view(), name='page-container-detail'),
    path('page-contained-jumbotrons/<int:pk>/', 
        PageContainedJumbotronDetailView.as_view(), 
        name='page-contained-jumbotron-detail', 
        ),    
    path('page-contained-events/<int:pk>/', 
        PageContainedEventDetailView.as_view(), 
        name='page-contained-event-detail', 
        ),
    path('page-contained-projects/<int:pk>/', 
        PageContainedProjectDetailView.as_view(), 
        name='page-contained-project-detail', 
        )                          
]