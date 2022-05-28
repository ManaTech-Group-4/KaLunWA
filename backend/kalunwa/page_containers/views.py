from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import (
    AllowAny,
     IsAuthenticated, 
     IsAuthenticatedOrReadOnly
)

from kalunwa.page_containers.models import PageContainer

from .serializers import HomePageContainerSerializer, PageContainerSerializer
# Create your views here.

# works, 
    #   readAPIView
    # listAPIView
    # ListModelMixin, GenericAPIView -> doesn't work

class PageContainerListView(ListCreateAPIView):# GenericAPIView, ListModelMixin, RetrieveModelMixin
    # permission_classes = (IsAuthenticatedOrReadOnly,)    
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer
    # slug of the object is not see in this case 

class PageContainerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer
    lookup_field = 'slug'


# /api/page-containers/<lookup>
# /api/page-containers/homepage
# /api/page-containers/organization-structure

