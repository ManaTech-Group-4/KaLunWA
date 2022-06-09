from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import (
    AllowAny,
     IsAuthenticated, 
     IsAuthenticatedOrReadOnly
)
from kalunwa.core.views import MultipleFieldLookupORMixin
from kalunwa.page_containers.models import (
    PageContainedJumbotron,
    PageContainedEvent,
    PageContainedProject,
    PageContainer,
)
from .serializers import (
    PageContainedJumbotronSerializer, 
    PageContainedEventSerializer,
    PageContainedProjectSerializer,
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

class PageContainedEventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainedEvent.objects.all()
    serializer_class = PageContainedEventSerializer    


class PageContainedProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PageContainedProject.objects.all() 
    serializer_class = PageContainedProjectSerializer       

# /api/page-containers/<lookup>
# /api/page-containers/<slug:slug>/contained_jumbotrons/<int:>
# /api/page-containers/organization-structure

