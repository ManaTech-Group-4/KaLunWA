from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Image, Jumbotron, Announcement
from .serializers import ImageSerializer, JumbotronSerializer, AnnouncementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
# url should be /admin

# stuff here are crammed pa

class ImageViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
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
        serializer = JumbotronSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Jumbotron.objects.all()
        jumbotron = get_object_or_404(queryset, pk=pk)
        serializer = JumbotronSerializer(jumbotron)
        return Response(serializer.data)

class AnnouncementViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Announcement.objects.all()
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Announcement.objects.all()
        jumbotron = get_object_or_404(queryset, pk=pk)
        serializer = AnnouncementSerializer(jumbotron)
        return Response(serializer.data)


#-------------------------------------------------------

class ImageUploadView(APIView): # untested
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
