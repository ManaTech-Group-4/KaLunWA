from django import views
from django.shortcuts import get_object_or_404
from .models import Event, Image, Jumbotron, Announcement, Project, News
from .serializers import EventSerializer,HomepageEventSerializer, HomepageJumbotronSerializer, HomepageNewsSerializer, HomepageProjectSerializer, ImageSerializer, JumbotronSerializer, AnnouncementSerializer, ProjectSerializer, NewsSerializer
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
    
    @action(detail=False)
    def news(self, request):
        news = News.objects.order_by('-created_at')[:3]
        serializer = HomepageNewsSerializer (news, many=True,context={'request':request})
        return Response(serializer.data)    

#------------------------------------------------------- 

class ImageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving images.
    """
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class JumbotronViewSet(viewsets.ModelViewSet):
    serializer_class = JumbotronSerializer
    queryset = Jumbotron.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    

class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


#-------------------------------------------------------
# Prep for file uploading
# 
# class ImageUploadView(APIView): 
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
# #        print(request.data)
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else: 
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
