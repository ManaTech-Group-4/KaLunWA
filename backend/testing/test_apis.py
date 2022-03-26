from django.test import RequestFactory
from django.urls import reverse
from django.db.models import Sum
from rest_framework.test import APITestCase
from .utils import get_expected_image_url, get_test_image_file
from kalunwa.content.models import CampEnum, CampLeader, CampPage, Demographics,  Image, Jumbotron, News, OrgLeader, Project, Tag, Event
from rest_framework import status

#-------------------------------------------------------------------------------
# HomePage Website
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
                name=f'image_{_}',
                image=image_file,
            )            

        # create content

        # fixed test date instead of timezone.now, so data can be compared
        cls.test_date = '2022-03-19 14:35:46.271745+00:00'

        for _ in range(3): # pks 0-2; 3 objects
        # create Jumbotrons
            Jumbotron.objects.create(
            header_title= f'Jumbotron {_}', 
            subtitle= f'short description {_}',
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
            is_published=True,
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
            is_published=True,
            )            

        # create News 
            News.objects.create(
                title = f'News {_}',
                description= f'description {_}',
                image = Image.objects.get(pk=_),
                is_published=True,
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
            is_published=True,
            )   

            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=cls.test_date,
            end_date=cls.test_date,
            camp=CampEnum.GENERAL,
            image = Image.objects.get(pk=_),
            is_featured=False,
            is_published=True,
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
       
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # checks if all generated jumbotrons were fetched
        self.assertEqual(len(self.jumbotrons), len(response.data))


    def test_get_homepage_events(self):
        """
        Note that this view only retrieves featured events, with a limit of 3.
        Requirement for fetched objects should be is_featured.
        """
        response = self.client.get(reverse("homepage-events"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(self.featured_events), len(response.data))

    def test_get_homepage_projects(self):
        response = self.client.get(reverse("homepage-projects"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(self.featured_projects), len(response.data))

    def test_get_homepage_news(self):
        response = self.client.get(reverse("homepage-news"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(self.news), len(response.data))

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
            response_jumbotron['subtitle'], 
            expected_jumbotron.subtitle
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
        response_news = response.data[0] # the latest is expected to be first on the list 
        image_url = get_expected_image_url(expected_news.image.image.name, request)
        self.assertEqual(response_news['title'], expected_news.title)
        self.assertEqual(response_news['description'], expected_news.description)
        self.assertEqual(response_news['image'], image_url)
        self.assertEqual(response_news['date'], expected_news.homepage_date())


#-------------------------------------------------------------------------------
# About Us Website
class AboutUsActionsTestCase(APITestCase):
    """
    Test about-us endpoints:
        about-us-demographics
        about-us-camps
        about-us-organization_leaders
    """
    @classmethod
    def setUpTestData(cls):

        test_image = get_test_image_file()

        # demographics data
        loc_1 = 40
        loc_2 = 30
        loc_3 = 17

        Demographics.objects.create(
            location = 'Tagbilaran',
            member_count = loc_1
        )

        Demographics.objects.create(
            location = 'Jagna',
            member_count = loc_2
        )

        Demographics.objects.create(
            location = 'Anda',
            member_count = loc_3
        )        

        # class attribute
        cls.total_members = loc_1 + loc_2 + loc_3

        # camp data

        for _ in range(5):
            Image.objects.create(
                name = f'camp default {_}',
                image = test_image
            )  
            # camp pages    
        CampPage.objects.create(
            name=CampEnum.SUBA.value,
            description = 'default description',
            image = Image.objects.get(name='camp default 0')
        )

        CampPage.objects.create(
            name=CampEnum.BAYBAYON.value,
            description = 'default description',
            image = Image.objects.get(name='camp default 1')
        )

        CampPage.objects.create(
            name=CampEnum.ZEROWASTE.value,
            description = 'default description',
            image = Image.objects.get(name='camp default 2')
        )

        CampPage.objects.create(
            name=CampEnum.LASANG.value,
            description = 'default description',
            image = Image.objects.get(name='camp default 3')        
        )

        # is unlikely, but for testing purposes 
        CampPage.objects.create(
            name=CampEnum.GENERAL.value,
            description = 'default description',
            image = Image.objects.get(name='camp default 4')        
        )
            # camp leaders
        for _ in range(4):
            dummy_image = Image.objects.create(
                name = f'camp leader {_}',
                image = test_image
            )   

            CampLeader.objects.create(
                first_name = f'firstname {_}',
                last_name = f'lastname {_}',
                background = f'background {_}',
                advocacy = f'advocacy {_}',
                position = CampLeader.Positions.LEADER,
                image=dummy_image
            )
        camps = [CampEnum.BAYBAYON, CampEnum.SUBA, CampEnum.LASANG, CampEnum.ZEROWASTE]

            # assigning respective camps, field is initially GNRL
        for _ in range(4):
            current_leader = CampLeader.objects.get(pk=_+1)
            current_leader.camp = camps[_] # 0-3
            current_leader.save()

        # organization leaders

        for _ in range (5):
            OrgLeader.objects.create(
                first_name = 'Extra',
                last_name = 'Leader',
                background = 'background',
                advocacy = 'advocacy',
                position = OrgLeader.Positions.OTHER,
                
                image=Image.objects.create(
                    name = 'other',
                    image = 'images/content/event.jpg'
                )
            )

        cls.camp_count = 4
        cls.org_leader_limit = 5
        cls.request_factory = RequestFactory()

    def test_get_demographics(self):
        response = self.client.get(reverse("about-us-demographics"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)    

    def test_get_camps(self):
        """
        - tests endpoint 
        - number of camps returned (4)
        - expected camps returned (Suba, Baybayon, Lasang, ZeroWaste)
        """
        response = self.client.get(reverse("about-us-camps"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)  
        self.assertEqual( self.camp_count, len(response.data))

        # test for duplicate camps (unlikely due to unique constraint)
        camps = CampEnum.labels
        camps.remove(CampEnum.GENERAL.label)
        response_camps = []
        for camp in response.data:
            response_camps.append(camp['camp_name'])
        
        # at this point camp count had already been checked (4 camps), so
            # making it a set would eliminate duplicates and expose if there is 
            # a missing camp
        self.assertEqual(set(camps), set(response_camps))

    def test_get_organization_leaders(self):
        response = self.client.get(reverse("about-us-organization-leaders"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)  
        self.assertEqual( self.org_leader_limit, len(response.data))  

    def test_get_demographics_data(self):
        response = self.client.get(reverse("about-us-demographics"))  
        self.assertEqual(response.data['total_members'], self.total_members)

    def test_get_camps_data(self):
        request = self.request_factory.get(reverse("about-us-camps"))
        response = self.client.get(reverse("about-us-camps"))

        # [1] get response data for a single camp 
        # [2] getting campname value (e.g. SB) to make it possible to match a query,
            # [3] by using the campname value to get the matching camp object created 

        response_camp = response.data[0] # [1]
        campname_value = self.get_camp_value_via_label(response_camp['camp_name']) # [2]
        expected_camp = CampPage.objects.get(name=campname_value) # [3]

        self.assertEqual(response_camp['camp_name'], expected_camp.get_name_display())
        camp_image_url = get_expected_image_url(expected_camp.image.image.name, request)
        self.assertEqual(response_camp['camp_image'],camp_image_url)
        
        expected_leader = CampLeader.objects.get(camp=campname_value)
        response_leader = response_camp['camp_leader']
        self.assertEqual(response_leader['name'], expected_leader.get_fullname())
        self.assertEqual(response_leader['motto'], expected_leader.motto)
        leader_image_url = get_expected_image_url(expected_leader.image.image.name, request)
        self.assertEqual(response_leader['image'],leader_image_url)
    
    def test_get_organization_leaders_data(self):
        request = self.request_factory.get(reverse("about-us-organization-leaders"))        
        response = self.client.get(reverse("about-us-organization-leaders"))  
        response_leader = response.data[0] 
        expected_leader = OrgLeader.objects.get(pk=response_leader['leader_id'])
        leader_image_url = get_expected_image_url(expected_leader.image.image.name, request)
        self.assertEqual(response_leader['image_url'], leader_image_url)       


        # utility functions
    def get_camp_value_via_label(self, label):
        if label == CampEnum.BAYBAYON.label:
            return CampEnum.BAYBAYON.value
        if label == CampEnum.SUBA.label:
            return CampEnum.SUBA.value
        if label == CampEnum.LASANG.label:
            return CampEnum.LASANG.value
        if label == CampEnum.ZEROWASTE.label:
            return CampEnum.ZEROWASTE.value
        if label == CampEnum.GENERAL.label:
            return CampEnum.GENERAL.value

        return None

# ---------------------------------------------------------------------------        
# Post end-points
# covers post serializer 

class NewsSerializerTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create image
        image = Image.objects.create(
                name='image_1',
                image=get_test_image_file(),
            )          

        cls.news = News.objects.create(
                title = 'News 1',
                description= 'description 1',
                image = Image.objects.get(pk=1),
                is_published=True,
            )        
        
    def test_news_validation_post(self):
        response = self.client.post(reverse('news-list'))

