
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.views import APIView
from .utils import HOMEPAGE_EVENT_URL, HOMEPAGE_JUMBOTRON_URL, HOMEPAGE_NEWS_URL, HOMEPAGE_PROJECT_URL, get_test_image_file, get_expected_image_url
from kalunwa.content.models import CampEnum, CampLeader, CampPage, Image, Jumbotron, News, Project, Tag, Event
from kalunwa.content.serializers import AboutUsCampSerializer, EventSerializer, HomepageJumbotronSerializer, HomepageNewsSerializer, HomepageProjectSerializer, JumbotronSerializer, ProjectSerializer
from kalunwa.content.serializers import StatusEnum


class ImageURLSerializerTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):

        cls.image = Image.objects.create(
            name='eating_me',
            image=get_test_image_file(),
        )

        cls.jumbotron = Jumbotron.objects.create(
            id=1, 
            header_title= 'J1', 
            subtitle= 'short description 1',
            image = cls.image
        )

        test_date = '2022-03-19 14:35:46.271745+00:00'

        cls.event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=1),
            is_featured=True,
            is_published=True,
            ) 

        cls.project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=test_date,
            end_date=test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=1),
            is_featured=False,
            is_published=True,
            )   

        cls.news = News.objects.create(
                title = 'News 1',
                description= 'description 1',
                image = Image.objects.get(pk=1),
                is_published=True,
            )

        cls.request_factory = APIRequestFactory()
        cls.image_file_name = cls.image.image.name

    # def get_expected_image_url(self, request):
    #     return f'{request.scheme}://{request.get_host()}/media/{self.image.image.name}'

    def test_get_object_image_pk(self):
        """
        test for:
        image = Image.objects.get(pk=obj.image.pk)
        """
        image = Image.objects.get(pk=self.jumbotron.image.id)
        self.assertEqual(self.image, image)
        

    def test_jumbotron_image_full_url(self):
        request = self.request_factory.get(HOMEPAGE_JUMBOTRON_URL)
        request = APIView().initialize_request(request) # convert to DRF request since WSGIRequest has no query params
        serializer = JumbotronSerializer(self.jumbotron, context={'request':request})
        ## build complete url 
            # request.scheme -> http
            # request.get_host() -> testserver        
            # self.image.image.name ->  images/content/test_U5U97df.jpg
        self.assertEqual(get_expected_image_url(self.image_file_name, request), serializer.data['image']['image'])

    def test_event_image_full_url(self):
        request = self.request_factory.get(HOMEPAGE_EVENT_URL)
        request = APIView().initialize_request(request)       
        serializer = EventSerializer(self.event, context={'request':request})
        self.assertEqual(get_expected_image_url(self.image_file_name, request), serializer.data['image']['image']) # might do image.url

    def test_project_image_full_url(self):
        request = self.request_factory.get(HOMEPAGE_PROJECT_URL)
        request = APIView().initialize_request(request)        
        serializer = ProjectSerializer(self.project, context={'request':request})
        self.assertEqual(get_expected_image_url(self.image_file_name, request), serializer.data['image']['image'])

    def test_news_image_full_url(self):
        request = self.request_factory.get(HOMEPAGE_NEWS_URL)
        request = APIView().initialize_request(request)             
        serializer = HomepageNewsSerializer(self.news, context={'request':request})
        self.assertEqual(get_expected_image_url(self.image_file_name, request), serializer.data['image'])


class AboutUsCampSerializertestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None: 
        # create camp -> Suba
        # create leader -> Suba, Cl
        test_image = get_test_image_file()

        CampPage.objects.create(
            name=CampEnum.SUBA.value,
            description = 'default description',
            image = Image.objects.create(
                name='suba',
                image=test_image
            )
        )
        
        CampPage.objects.create(
            name=CampEnum.BAYBAYON.value,
            description = 'default description',
            image = Image.objects.create(
                name='camp',
                image=test_image
            )
        )        

        CampLeader.objects.create(
            first_name = 'Suba',
            last_name = 'Asub',
            background = 'background',
            advocacy = 'advocacy',
            position = CampLeader.Positions.LEADER,
            camp=CampEnum.SUBA,
            image= Image.objects.create(
                name='suba_lead',
                image=test_image
            )
        )

        CampLeader.objects.create(
            first_name = 'Baybayon',
            last_name = 'Noyabyab',
            background = 'background',
            advocacy = 'advocacy',
            position = CampLeader.Positions.ASSISTANT_LEADER,
            camp=CampEnum.BAYBAYON,
            image= Image.objects.create(
                name='baybayon_AL',
                image=test_image
            )
        )        
        # create camp that has no Camp leader -> Baybayon
        # create leader -> Suba, Al
    def test_serialize_with_camp_leader(self):
        """
        test to serialize camp details when a camp leader exists
        """
        camp_with_leader = CampPage.objects.get(name=CampEnum.SUBA)
        serializer = AboutUsCampSerializer(camp_with_leader)
        
        self.assertTrue(serializer.data['camp_leader']) # exists

    def test_serialize_without_camp_leader(self):
        """
        test to serialize camp details when a camp leader does not exists.
        returns none, or a non-truthy value (false)
        """
        camp_without_leader = CampPage.objects.get(name=CampEnum.BAYBAYON)
        serializer = AboutUsCampSerializer(camp_without_leader)
        self.assertFalse(serializer.data['camp_leader']) # does not exist (null)

class StatusSerializerTestCase(TestCase):
    """
    test dates are prepared to simulate a timezone.now() request, and
    get the expected status
    """
    @classmethod
    def setUpTestData(cls) -> None: 
        date_tomorrow = timezone.now() + timezone.timedelta(days=1)
        date_yesterday = timezone.now() - timezone.timedelta(days=1)

        image_file = get_test_image_file()
 
        for _ in range(4): 
            Image.objects.create(
                pk=_,
                name=f'image_{_}',
                image=image_file,
            )

        image = Image.objects.create(
                name='image_1',
                image=get_test_image_file(),            

        )
        # events
            #  upcoming
        cls.event_upcoming = Event.objects.create(
            title= 'upcoming event', 
            description= 'description 1',
            start_date=date_tomorrow,
            end_date=date_tomorrow,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=1),
            is_featured=True,
            is_published=True,
        ) 
            #  ongoing            
        cls.event_ongoing = Event.objects.create(
            title= 'ongoing event', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=date_tomorrow,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=2),
            is_featured=True,
            is_published=True,
        ) 

            #  past            
        cls.event_past = Event.objects.create(
            title= 'past event', 
            description= 'description 1',
            start_date=date_yesterday,
            end_date=date_yesterday,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=3),
            is_featured=True,
            is_published=True,
        ) 

        #projects 
            # upcoming
        cls.project_upcoming = Project.objects.create(
            title= 'upcoming project', 
            description= 'description 1',
            start_date=date_tomorrow,
            end_date=date_tomorrow,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=1),
            is_featured=True,
            is_published=True,
        ) 
            #  ongoing            
        cls.project_ongoing = Project.objects.create(
            title= 'ongoing project', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=date_tomorrow,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=2),
            is_featured=True,
            is_published=True,
        ) 
            #no_end date, ongoing
        cls.project_ongoing_no_end_date = Project.objects.create(
            title= 'ongoing project no end date', 
            description= 'description 1',
            start_date=timezone.now(),
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=3),
            is_featured=True,
            is_published=True,
        ) 

            #  past            
        cls.project_past = Project.objects.create(
            title= 'past project', 
            description= 'description 1',
            start_date=date_yesterday,
            end_date=date_yesterday,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=4),
            is_featured=True,
            is_published=True,
        ) 

    def test_past_status_event(self):
        serializer = EventSerializer(self.event_past)
        self.assertEqual(serializer.data['status'], StatusEnum.PAST.value)

    def test_ongoing_status_event(self):
        serializer = EventSerializer(self.event_ongoing)
        self.assertEqual(serializer.data['status'], StatusEnum.ONGOING.value)

    def test_upcoming_status_event(self):
        serializer = EventSerializer(self.event_upcoming)
        self.assertEqual(serializer.data['status'], StatusEnum.UPCOMING.value)

    def test_past_status_project(self):
        serializer = ProjectSerializer(self.project_past)
        self.assertEqual(serializer.data['status'], StatusEnum.PAST.value)

    def test_ongoing_status_project(self):
        serializer = ProjectSerializer(self.project_ongoing)
        self.assertEqual(serializer.data['status'], StatusEnum.ONGOING.value)

    def test_ongoing_no_date_status_project(self):
        serializer = ProjectSerializer(self.project_ongoing_no_end_date)
        self.assertEqual(serializer.data['status'], StatusEnum.ONGOING.value)

    def test_upcoming_status_project(self):
        serializer = ProjectSerializer(self.project_upcoming)
        self.assertEqual(serializer.data['status'], StatusEnum.UPCOMING.value)

