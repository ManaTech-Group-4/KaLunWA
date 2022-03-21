from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from kalunwa.content.serializers import StatusEnum
from .utils import get_test_image_file
from kalunwa.content.models import CampEnum, Image, Jumbotron, News, Project, Tag, Event
from rest_framework import status


class HomapageActionsTestCase(APITestCase):
    """
    Test homepage endpoints:
        homepage-jumbotrons
        homepage-events
        homepage-projects
        homepage-news
    """
    @classmethod
    def setUpTestData(cls):
        """
        set ups data that will not be changed in the class. 
        vs. 
        setUp, expects changes & refreshes for every test method.
        """
        
        # create Image objects

        image_file = get_test_image_file()
 
        for _ in range(7): # create 6 for featured & unfeatured content
            Image.objects.create(
                pk=_,
                title=f'image_{_}',
                image=image_file,
            )            

        # create content

        # fixed test date instead of timezone.now, so data can be compared
        test_date = '2022-03-19 14:35:46.271745+00:00'

        for _ in range(3): # pks 0-2; 3 objects
        # create Jumbotrons
            Jumbotron.objects.create(
            header_title= f'Jumbotron {_}', 
            short_description= f'short description {_}',
            image = Image.objects.get(pk=_)
            )

        # create Events (featured) 
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=True,
            )            

        # create Projects (featured) 
            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=True,
            )            

        # create News 
            News.objects.create(
                title = f'News {_}',
                description= f'description {_}',
                image = Image.objects.get(pk=_),
            )

        # create non-featured Events and Projects
        for _ in range(3,6): # pks 3 - 5; 3 objects
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=False,
            )   

            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=False,
            )   

        ## class attributes: lists of respective objects
        cls.jumbotrons = Jumbotron.objects.all()
        cls.featured_events = Event.objects.filter(is_featured=True)
        cls.featured_projects = Project.objects.filter(is_featured=True)
        cls.news = News.objects.all()


    def test_get_homepage_jumbotrons(self):
        """
        Tests list endpoints for homepage jumbotrons.
        """
        # reverse returns (/api/homepage/jumbotrons/)
        response = self.client.get(reverse("homepage-jumbotrons"))
        
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        # checks if all generated jumbotrons were fetched
        self.assertEquals(len(self.jumbotrons), len(response.data))


    def test_get_homepage_events(self):
        """
        Note that this view only retrieves featured events, with a limit of 3.
        Requirement for fetched objects should be is_featured.
        """
        response = self.client.get(reverse("homepage-events"))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.featured_events), len(response.data))

    def test_get_homepage_projects(self):
        response = self.client.get(reverse("homepage-projects"))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.featured_projects), len(response.data))

    def test_get_homepage_news(self):
        response = self.client.get(reverse("homepage-news"))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.news), len(response.data))
        
  
# ---------------------------------------------------------------------------        
