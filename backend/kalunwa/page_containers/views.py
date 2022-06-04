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
from kalunwa.core.views import MultipleFieldLookupORMixin
from kalunwa.page_containers.models import PageContainedJumbotron, PageContainer
from .serializers import (
    PageContainedJumbotronSerializer, 
    PageContainerSerializer,
    PageContainerReadSerializer,
    )
# Create your views here.

class PageContainerListView(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)    
    queryset = PageContainer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':        
            return PageContainerReadSerializer
        return PageContainerSerializer


class PageContainerDetailView(MultipleFieldLookupORMixin, RetrieveUpdateDestroyAPIView):
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer
    lookup_fields = ['slug', 'id']

    def get_serializer_class(self):
        if self.request.method == 'GET':        
            return PageContainerReadSerializer
        return PageContainerSerializer


class PageContainedJumbotronDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainedJumbotron.objects.all()
    serializer_class = PageContainedJumbotronSerializer

# /api/page-containers/<lookup>
# /api/page-containers/<slug:slug>/contained_jumbotrons/<int:>
# /api/page-containers/organization-structure

