from django.db.models import Sum
from .models import CampEnum, Event, Image, Jumbotron, Announcement, Project, News
from .models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer
from .serializers import AboutUsCampSerializer, AboutUsLeaderImageSerializer, EventSerializer,HomepageJumbotronSerializer, HomepageNewsSerializer, HomepageProjectSerializer, ImageSerializer, ImageURLSerializer, JumbotronSerializer, AnnouncementSerializer, ProjectSerializer, NewsSerializer
from .serializers import DemographicsSerializer, CampPageSerializer, OrgLeaderSerializer, CommissionerSerializer, CampLeaderSerializer, CabinOfficerSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

  
class EventViewSet(viewsets.ModelViewSet): 
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(detail=False)
    def homepage(self, request):
         # possible to filter data in url, but limit would have to be implemented in finalize response
         # or have limit implemented inside via a pagination (limitoffsetpagination)
        queryset= Event.objects.filter(is_featured=True)[:3]
        serializer = self.serializer_class(queryset, many=True, context={'request':request})
        return Response(serializer.data)


    # might need to add new serializer field for non-read only stuff that needs
    # to be posted data on (or let frontend manipulate the dates nlng)
#-------------------------------------------------------------------------------
# homepage views


class HomepageViewSet(viewsets.ViewSet):

    @action(detail=False)
    def jumbotrons(self, request):
        jumbotrons = Jumbotron.objects.all()
        # passing context from the request, for the serializer to use
        serializer = HomepageJumbotronSerializer(jumbotrons, many=True, context={'request':request})
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

#-------------------------------------------------------------------------------
# about us view

class AboutUsViewset(viewsets.ViewSet):
    @action(detail=False)
    def demographics(self, request):
        return Response(Demographics.objects.aggregate(total_members=Sum('member_count')))
    
    @action(detail=False)
    def camps(self, request):
        # ensures 1 of each camp incase of duplicates
        suba = CampPage.objects.filter(name=CampEnum.SUBA) [:1]
        baybayon = CampPage.objects.filter(name=CampEnum.BAYBAYON) [:1]
        zero_waste = CampPage.objects.filter(name=CampEnum.ZEROWASTE) [:1]
        lasang = CampPage.objects.filter(name=CampEnum.LASANG) [:1]

        camps = suba | baybayon | zero_waste | lasang # combines into one queryset

        serializer = AboutUsCampSerializer(camps, many=True, context={'request':request})
        return Response(serializer.data)
    
    @action(detail=False)
    def organization_leaders(self, request):
        org_leaders = OrgLeader.objects.all()[:5]
        serializer = AboutUsLeaderImageSerializer(org_leaders, many=True, context={'request':request})
        return  Response(serializer.data)


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




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-----------------------------newly added models as of 23/3/2022-------------------------------------------------

class DemographicsViewSet(viewsets.ModelViewSet):
    serializer_class = DemographicsSerializer
    queryset = Demographics.objects.all()

class CampPageViewSet(viewsets.ModelViewSet):
    serializer_class = CampPageSerializer
    queryset = CampPage.objects.all()

class OrgLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = OrgLeaderSerializer
    queryset = OrgLeader.objects.all()

class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializer
    queryset = Commissioner.objects.all()

class CampLeaderViewSet(viewsets.ModelViewSet):
    serializer_class = CampLeaderSerializer
    queryset = CampLeader.objects.all()

class CabinOfficerViewSet(viewsets.ModelViewSet):
    serializer_class = CabinOfficerSerializer
    queryset = CabinOfficer.objects.all()