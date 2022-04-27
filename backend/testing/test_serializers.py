
from django.test import TestCase
from django.utils import timezone
from .utils import  get_test_image_file
from kalunwa.content.models import CampEnum, CampLeader, CampPage, Image, Project, Event
from kalunwa.content.serializers import CampPageSerializer, EventSerializer, ProjectSerializer
from kalunwa.content.serializers import StatusEnum


class CampSerializertestCase(TestCase):
    """
    - test to serialize camp details when a camp leader exists
    - test to serialize camp details when a camp leader does not exists.
        returns none, or a non-truthy value (false)
    # test if camp has doubles? will be restricted for posting so it would be hard to replicate
    """
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
            quote = 'quote',
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
            quote = 'quote',
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
        serializer = CampPageSerializer(camp_with_leader)
        
        self.assertTrue(serializer.data['camp_leader']) # exists

    def test_serialize_without_camp_leader(self):
        """
        test to serialize camp details when a camp leader does not exists.
        returns none, or a non-truthy value (false)
        """
        camp_without_leader = CampPage.objects.get(name=CampEnum.BAYBAYON)
        serializer = CampPageSerializer(camp_without_leader)
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

