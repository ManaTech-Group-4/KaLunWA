from django.urls import path, include
from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    PageContainerListView,
    PageContainerDetailView,
    PageContainedJumbotronDetailView,
)

urlpatterns = [
    path('page-containers/', PageContainerListView.as_view(), name='page-container-list'),
    path('page-containers/<int:pk>/', PageContainerDetailView.as_view(), name='page-container-detail'),    
    path('page-containers/<slug:slug>/', PageContainerDetailView.as_view(), name='page-container-detail'),
    path('page-contained-jumbotrons/<int:pk>/', 
        PageContainedJumbotronDetailView.as_view(), 
        name='page-contained-jumbotron-detail', 
        )    
]