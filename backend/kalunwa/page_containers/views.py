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

from kalunwa.page_containers.models import PageContainedJumbotron, PageContainer

from .serializers import HomePageContainerSerializer, PageContainedJumbotronSerializer, PageContainerSerializer
# Create your views here.


class PageContainerListView(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)    
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer

class PageContainerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer
    lookup_field = 'slug'


class PageContainedJumbotronDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainedJumbotron.objects.all()
    serializer_class = PageContainedJumbotronSerializer

# /api/page-containers/<lookup>
# /api/page-containers/<slug:slug>/contained_jumbotrons/<int:>
# /api/page-containers/organization-structure

