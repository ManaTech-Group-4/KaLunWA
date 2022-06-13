from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
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
from kalunwa.content.views import AssignLastUpdatedBy
from kalunwa.users.permissions import AuthenticatedAndReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PageContainerListView(AssignLastUpdatedBy, ListCreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]   
    queryset = PageContainer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':        
            return PageContainerReadSerializer
        return PageContainerSerializer


class PageContainerDetailView(AssignLastUpdatedBy, MultipleFieldLookupORMixin, RetrieveUpdateDestroyAPIView):
    queryset = PageContainer.objects.all()
    serializer_class = PageContainerSerializer
    lookup_fields = ['slug', 'id']
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':        
            return PageContainerReadSerializer
        return PageContainerSerializer


class DestroyAndAssignObjectToHomePageMixin:
    def assign_editor_to_homepage(self):
        # grab request user, assign it to homepage. though we have to grab 
        # homepage before deletion happens
        try:
            homepage = PageContainer.objects.get(name='homepage')
            homepage.last_updated_by = self.request.user
            homepage.save()
        except Exception:
            pass

    def perform_destroy(self, instance):
        instance.delete()
        # update whoever deleted / removed the link of the two 
        self.assign_editor_to_homepage()
        

class PageContainedJumbotronDetailView(DestroyAndAssignObjectToHomePageMixin, RetrieveUpdateDestroyAPIView):
    queryset = PageContainedJumbotron.objects.all()
    serializer_class = PageContainedJumbotronSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]



class PageContainedEventDetailView(DestroyAndAssignObjectToHomePageMixin, RetrieveUpdateDestroyAPIView):
    queryset = PageContainedEvent.objects.all()
    serializer_class = PageContainedEventSerializer    
    permission_classes=[IsAuthenticatedOrReadOnly]    


class PageContainedProjectDetailView(DestroyAndAssignObjectToHomePageMixin, RetrieveUpdateDestroyAPIView):
    queryset = PageContainedProject.objects.all() 
    serializer_class = PageContainedProjectSerializer   
    permission_classes=[IsAuthenticatedOrReadOnly]        
