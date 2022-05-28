from django.urls import path, include
from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    PageContainerListView,
    PageContainerDetailView
)

urlpatterns = [
    path('page-containers/', PageContainerListView.as_view(), name='page-container-list'),
    # path('page-containers/<pk>/', PageContainerView.as_view(), name='page-container-detail')    
    path('page-containers/<slug:slug>/', PageContainerDetailView.as_view(), name='page-container-detail')
]
#^cabinofficers/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$





 