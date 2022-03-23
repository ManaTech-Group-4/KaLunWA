<<<<<<< HEAD
from django.test import RequestFactory, TestCase #removed this from main
=======
from math import exp
from django.test import RequestFactory, TestCase
>>>>>>> 2fd88ca172eda58ac7a538d95fcc64ca113a0b0d
from django.urls import reverse
from django.utils import timezone 
from rest_framework.test import APITestCase
<<<<<<< HEAD
from kalunwa.content.serializers import StatusEnum #removed from main
from .utils import get_test_image_file
=======
from kalunwa.content.serializers import StatusEnum
from .utils import get_expected_image_url, get_test_image_file
>>>>>>> 2fd88ca172eda58ac7a538d95fcc64ca113a0b0d
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
        cls.test_date = '2022-03-19 14:35:46.271745+00:00'

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
            start_date=cls.test_date,
            end_date=cls.test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=True,
            )            

        # create Projects (featured) 
            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=cls.test_date,
            end_date=cls.test_date,
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
            start_date=cls.test_date,
            end_date=cls.test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=False,
            )   

            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=cls.test_date,
            end_date=cls.test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=False,
            )   

        ## class attributes: lists of respective objects
        cls.jumbotrons = Jumbotron.objects.all()
        cls.featured_events = Event.objects.filter(is_featured=True)
        cls.featured_projects = Project.objects.filter(is_featured=True)
        cls.news = News.objects.all()
        cls.image = Image.objects.get(pk=0)
        cls.image_file_name = cls.image.image.name
        cls.request_factory = RequestFactory()


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

    def test_get_expected_homepage_jumbotron_data(self):
        # need request to build image full url (request scheme, host)
        request = self.request_factory.get(reverse("homepage-jumbotrons"))
        response = self.client.get(reverse("homepage-jumbotrons")) 
        # gets the earliest object created within the range 
        expected_jumbotron = Jumbotron.objects.get(pk=self.jumbotrons[0].pk)
        response_jumbotron = response.data[0]
        image_url = get_expected_image_url(self.image_file_name, request)
        self.assertEqual(
            response_jumbotron['header_title'],
            expected_jumbotron.header_title
        )
        self.assertEqual(
            response_jumbotron['short_description'], 
            expected_jumbotron.short_description
            )
        self.assertEqual(response_jumbotron['image'], image_url)

    def test_get_expected_homepage_event_data(self):
        request = self.request_factory.get(reverse("homepage-events"))
        response = self.client.get(reverse("homepage-events"))  
        expected_event = Event.objects.get(pk=self.featured_events[0].pk)  
        response_event = response.data[0]
        image_url = get_expected_image_url(expected_event.image.image.name, request)
        self.assertEqual(response_event['title'],expected_event.title)
        self.assertEqual(response_event['image'], image_url)

    def test_get_expected_homepage_project_data(self):
        request = self.request_factory.get(reverse("homepage-projects"))
        response = self.client.get(reverse("homepage-projects"))  
        # latest featured project (1-3) (earliest -> latest)
        expected_project = Project.objects.get(pk=self.featured_projects[0].pk)  
        response_project = response.data[0]
        image_url = get_expected_image_url(expected_project.image.image.name, request)
        self.assertEqual(response_project['title'], expected_project.title)
        self.assertEqual(response_project['image'], image_url)
        
    def test_get_expected_homepage_news_data(self):
        request = self.request_factory.get(reverse("homepage-news"))
        response = self.client.get(reverse("homepage-news"))  
        expected_news = News.objects.latest('created_at')
        response_news = response.data[0] 
        image_url = get_expected_image_url(expected_news.image.image.name, request)
        self.assertEqual(response_news['title'], expected_news.title)
        self.assertEqual(response_news['description'], expected_news.description)
        self.assertEqual(response_news['image'], image_url)
        self.assertEqual(response_news['date'], expected_news.created_at.date())

# ---------------------------------------------------------------------------        
# Post end-points
# covers post serializer 

class NewsSerializerTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create image
        image = Image.objects.create(
                title='image_1',
                image=get_test_image_file(),
            )          

        cls.news = News.objects.create(
                title = 'News 1',
                description= 'description 1',
                image = Image.objects.get(pk=1),
            )        
        
    def test_news_validation_post(self):
        response = self.client.post(reverse('news-list'))

