from django.shortcuts import get_object_or_404
from .models import Event, Image, Jumbotron, Announcement, Project, News
from .serializers import EventSerializer,HomepageEventSerializer, HomepageJumbotronSerializer, HomepageProjectSerializer, ImageSerializer, JumbotronSerializer, AnnouncementSerializer, ProjectSerializer, NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

# Create your views here.
# url should be /admin
#-------------------------------------------------------
# homepage views

class HomepageViewSet(viewsets.ViewSet):

    @action(detail=False)
    def jumbotrons(self, request):
        jumbotrons = Jumbotron.objects.all()
        # passing context from the request, for the serializer to use
        serializer = HomepageJumbotronSerializer(jumbotrons, many=True, context={'request':request})
        return Response(serializer.data)

    @action(detail=False)
    def events(self, request):
        events = Event.objects.filter(is_featured=True)[:3]
        serializer = HomepageEventSerializer(events, many=True,context={'request':request})
        return Response(serializer.data)

    @action(detail=False)
    def projects(self, request):
        projects = Project.objects.filter(is_featured=True)[:3]
        serializer = HomepageProjectSerializer(projects, many=True,context={'request':request})
        return Response(serializer.data)    
    
    # news (query order by, get latest 3)

#------------------------------------------------------- 

class ImageViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    def list(self,request):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Image.objects.all()
        image = get_object_or_404(queryset, pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)


class JumbotronViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Jumbotron.objects.all()
        serializer = JumbotronSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Jumbotron.objects.all()
        jumbotron = get_object_or_404(queryset, pk=pk)
        serializer = JumbotronSerializer(jumbotron)
        return Response(serializer.data)


class EventViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

class NewsViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(news)
        return Response(serializer.data)

class AnnouncementViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Announcement.objects.all()
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Announcement.objects.all()
        announcement = get_object_or_404(queryset, pk=pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)




#-------------------------------------------------------

class ImageUploadView(APIView): # untested
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
#        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
