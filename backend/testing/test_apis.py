import json
from django.test import RequestFactory
from django.urls import reverse
from django.db.models import Sum
from django.utils import timezone
from rest_framework.test import APITestCase
from .utils import get_camp_value_via_label, get_expected_image_url, get_test_image_file, to_formal_mdy
from kalunwa.content.models import CampEnum, CampLeader, CampPage, Demographics,  Image, Jumbotron, News, OrgLeader, Project, Tag, Event
from rest_framework import status
#-------------------------------------------------------------------------------
# HomePage Website

class HomepageJumbotronsTestCase(APITestCase):
    """
    Test homepage endpoints:
        homepage-jumbotrons 
        reverse() of the above returns /api/homepage/jumbotrons/

    tests:
        test if request limit (5) is implemented
    
    """
    @classmethod
    def setUpTestData(cls):
        cls.jumbotron_limit = 5
        cls.image_file = get_test_image_file()
        cls.request_factory = RequestFactory()
    
    def test_get_homepage_jumbotrons(self):
        """
        Tests list endpoints for homepage jumbotrons, return OK code. Tests list limit. 
        mock: create 6 jumbotrons (limit + 1) to test if limiting logic works. 
        """
        # create 6 Image objects, given unique images per jumbotron are required.
        for _ in range(6): 
            Jumbotron.objects.create(
                header_title= f'Jumbotron {_}', 
                subtitle= f'short description {_}',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file)  
            )

        response = self.client.get(reverse("homepage-jumbotrons"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.jumbotron_limit) # a <= b
    
    def test_get_homepage_jumbotron_data(self):
        """
        Given no variation with serializing jumbotron data, retrieving and 
        checking only 1 for its content is enough. 

        Assumption: Jumbotron object has the appropriate fields.  
        """
        Jumbotron.objects.create(
            header_title= 'Jumbotron 1', 
            subtitle= 'short description',
            image = Image.objects.create(name=f'image_1', image=self.image_file)          
        )
        # need request to build image full url (request scheme, host)
        request = self.request_factory.get(reverse("homepage-jumbotrons"))
        response = self.client.get(reverse("homepage-jumbotrons")) 
       
        response_jumbotron = json.loads(response.content)[0] # json to python 
        expected_jumbotron = Jumbotron.objects.get(pk=response_jumbotron['id'])

        image_url = get_expected_image_url(expected_jumbotron.image.image.name, request)
        
        expected_jumbotron_data = {
            'id' : expected_jumbotron.id, 
            'header_title' : expected_jumbotron.header_title,
            'subtitle' : expected_jumbotron.subtitle,
            'image' : image_url
        }

        self.assertDictEqual(response_jumbotron, expected_jumbotron_data)


class HomepageEventsTestCase(APITestCase):
    """
    Test homepage endpoints:
        homepage-events 

        - test if request limit (3) is implemented
        - test if events are featured
    """
    @classmethod
    def setUpTestData(cls):
        """
        - separate test for featured events,
        - separate test for limit
        """
        cls.event_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = RequestFactory()

    
    def test_get_homepage_events(self):
        """
        Tests list endpoints for homepage events, return OK code. Tests list limit. 
        mock: all 4 are featured
        """
        # create 4 featured events
        for _ in range(4): 
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file),  
            is_featured=True,
            )   

        response = self.client.get(reverse("homepage-events"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.event_limit) # a <= b

    def test_get_homepage_featured_events(self):
        """
        Test if only featured events are returned. 
        mock: 2 featured and 3 non-featured.
        """

        for _ in range(5): 
            if _ == [0,1]: # first 2 events are featured, rest are not
                featured = True
            else:
                featured = False

            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            is_featured=featured,
        )                

        response = self.client.get(reverse("homepage-events")) 
        events = response.data

        for event in events:
            fetched_event = Event.objects.get(pk=event['id'])
            self.assertTrue(fetched_event.is_featured)
    
    def test_get_homepage_event_data(self):
        Event.objects.create(
        title= 'Event 1', 
        description= 'description 1',
        start_date=timezone.now(),
        end_date=timezone.now(),
        image = Image.objects.create(name='image_1', image=self.image_file),
        is_featured=True,
        )       

        request = self.request_factory.get(reverse("homepage-events"))
        response = self.client.get(reverse("homepage-events")) 
        
        event = json.loads(response.content)[0]
        expected_event = Event.objects.get(pk=event['id'])
        image_url = get_expected_image_url(expected_event.image.image.name, request)

        expected_event_data = {
            'id' : expected_event.id,
            'title' : expected_event.title,
            'image' : image_url
        } 
        self.assertDictEqual(event, expected_event_data)
    

class HomepageProjectsTestCase(APITestCase):
    """
    Test homepage endpoints:
        homepage-projects 

        - test if request limit (3) is implemented
        - test if projects are featured
    """
    @classmethod
    def setUpTestData(cls):
        """
        - separate test for featured projects,
        - separate test for limit
        """
        cls.project_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = RequestFactory()
    
    def test_get_homepage_projects(self):
        """
        Tests list endpoints for homepage projects, return OK code. Tests list limit. 
        mock: all 4 are featured
        """
        # create 4 featured events
        for _ in range(4): 
            Image.objects.create(
            pk=_,
            name=f'image_{_}',
            image=self.image_file,
        )       

        Project.objects.create(
        title= f'Project {_}', 
        description= f'description {_}',
        start_date=timezone.now(),
        end_date=timezone.now(),
        image = Image.objects.get(pk=_),
        is_featured=True,
        )   

        response = self.client.get(reverse("homepage-projects"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.project_limit) # a <= b

    def test_get_homepage_featured_projects(self):
        """
        Test if only featured projects are returned. 
        mock: 2 featured and 3 non-featured.
        """
        for _ in range(5): 
            if _ == [0,1]: # first 2 events are featured, rest are not
                featured = True
            else:
                featured = False

            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            is_featured=featured,
        )                 

        response = self.client.get(reverse("homepage-projects")) 
        projects = response.data

        for project in projects:
            fetched_project = Project.objects.get(pk=project['id'])
            self.assertTrue(fetched_project.is_featured)
    
    def test_get_homepage_event_data(self):
        Project.objects.create(
        title= 'Project 1', 
        description= 'description 1',
        start_date=timezone.now(),
        end_date=timezone.now(),
        image = Image.objects.create(name='image_1', image=self.image_file),
        is_featured=True,
        )       

        request = self.request_factory.get(reverse("homepage-projects"))
        response = self.client.get(reverse("homepage-projects")) 
        
        project = json.loads(response.content)[0]
        expected_project = Project.objects.get(pk=project['id'])
        image_url = get_expected_image_url(expected_project.image.image.name, request)

        expected_project_data = {
            'id' : expected_project.id,
            'title' : expected_project.title,
            'image' : image_url
        } 
        self.assertDictEqual(project, expected_project_data)


class HomepageNewsTestCase(APITestCase):
    """
    Test homepage endpoints:
        homepage-news 

        - test if request limit (3) is implemented
        - test if news are featured
    """
    @classmethod
    def setUpTestData(cls):
        """
        - separate test for latest news,
        - separate test for limit
        """
        cls.news_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = RequestFactory()

    
    def test_get_homepage_news(self):
        """
        Tests list endpoints for homepage news, return OK code. Tests list limit. 
        mock: all 4 are featured
        """
        # create 4 news
        for _ in range(4): 
            News.objects.create(
            title= f'News {_}', 
            description= f'description {_}',
            image = Image.objects.create( name=f'image_{_}', image=self.image_file)               
            )   

        response = self.client.get(reverse("homepage-news"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.news_limit) # a <= b

    def test_get_homepage_latest_news(self):
        """
        Test if only latest news are returned (latest at 1st index, 2nd at 2nd, etc.)
        Latest determined by largest pk value.
        mock: create 4 news 
        """
        for _ in range(1,5): # 1, 2, 3, 4
            News.objects.create(
            title= f'News {_}', 
            description= f'description {_}',
            image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
        )                

        response = self.client.get(reverse("homepage-news")) 
        news_set = response.data

        pk = 4
        for news in news_set:
            self.assertEqual(news['id'], pk)
            pk-=1
  
    def test_get_homepage_news_data(self):
        News.objects.create(
        title= 'News 1', 
        description= 'description 1',
        image = Image.objects.create(name='image_1', image=self.image_file),
        )   

        request = self.request_factory.get(reverse("homepage-news"))
        response = self.client.get(reverse("homepage-news")) 
        
        news = json.loads(response.content)[0]
        expected_news = News.objects.get(pk=news['id'])
        image_url = get_expected_image_url(expected_news.image.image.name, request)

        expected_news_data = {
            'id' : expected_news.id,
            'title' : expected_news.title,
            'description' : expected_news.description,
            'date' : to_formal_mdy(expected_news.created_at),
            'image' : image_url
        } 
        self.assertDictEqual(news, expected_news_data)

#-------------------------------------------------------------------------------
# About Us Website

class AboutUsDemographics(APITestCase):
    """
    Test about-us endpoints:    
        about-us-demographics    
    """
    @classmethod
    def setUpTestData(cls):
        # demographics data
        loc_1 = 40
        loc_2 = 30
        loc_3 = 17

        Demographics.objects.create(location = 'Tagbilaran', member_count = loc_1)
        Demographics.objects.create(location = 'Jagna', member_count = loc_2)
        Demographics.objects.create(location = 'Anda', member_count = loc_3)

        # class attribute
        cls.total_members = loc_1 + loc_2 + loc_3
        cls.request_factory = RequestFactory()        

    def test_get_demographics(self):
        response = self.client.get(reverse("about-us-demographics"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)    

    def test_get_demographics_data(self):
        response = self.client.get(reverse("about-us-demographics"))  
        self.assertEqual(response.data['total_members'], self.total_members)


class AboutUsCampsTestCase(APITestCase):
    """
    Test about-us endpoints:    
        about-us-camps    

        # 3 camps, lacking 1   
    """    

    @classmethod
    def setUpTestData(cls):    
        cls.camp_count = 4
        cls.test_image = get_test_image_file()
        cls.camps_values = CampEnum.values
        cls.camp_labels = CampEnum.labels
        cls.request_factory = RequestFactory()        

    def test_get_camps(self):
        """
        - tests endpoint 
        - number of camps returned (4)
        mock: 5 camps (expected + general)
        """

        for _ in range(5):
            # camp pages    
            CampPage.objects.create(
                name=self.camps_values[_],
                description = 'default description',
                image = Image.objects.create(name = 'name', image = self.test_image)
        )   
        
        response = self.client.get(reverse("about-us-camps"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)  
        self.assertEqual( self.camp_count, len(response.data))   

    def test_get_expected_camps_general(self):
        """
        - expected camps returned (Suba, Baybayon, Lasang, ZeroWaste)
        mock: 5 camps (expected + general)     
        """
        # mock data
        for _ in range(5):
            # camp pages    
            CampPage.objects.create(
                name=self.camps_values[_],
                description = 'default description',
                image = Image.objects.create(name = 'name', image = self.test_image)
            )   
        expected_camps = self.camp_labels
        expected_camps.remove(CampEnum.GENERAL.label)

        response = self.client.get(reverse("about-us-camps"))       
        response_camps = []
        for camp in response.data:
            response_camps.append(camp['camp_name']) 
        
        self.assertListEqual(sorted(expected_camps), sorted(response_camps))

    def test_get_expected_camps_duplicate(self):
        """
        - expected camps returned (Suba, Baybayon, Lasang, ZeroWaste)
        mock: # 5 camps + duplicate on 1 camp (suba)     
        """
        # mock data
        for _ in range(5):
            # camp pages    
            CampPage.objects.create(
                name=self.camps_values[_],
                description = 'default description',
                image = Image.objects.create(name = 'name', image = self.test_image)
            )                  
        CampPage.objects.create(
            name=CampEnum.SUBA.value,
            description='default',
                image = Image.objects.create(name = 'name', image = self.test_image)            
        )
        expected_camps = self.camp_labels
        expected_camps.remove(CampEnum.GENERAL.label)

        response = self.client.get(reverse("about-us-camps"))       
        response_camps = []
        for camp in response.data:
            response_camps.append(camp['camp_name']) 
        
        self.assertListEqual(sorted(expected_camps), sorted(response_camps))

    def test_get_camp_data(self):
        CampPage.objects.create(
            name=CampEnum.SUBA.value,
            description='default',
            image = Image.objects.create(name = 'name', image = self.test_image)            
        )        
        request = self.request_factory.get(reverse("about-us-camps"))
        response = self.client.get(reverse("about-us-camps"))  

        camp = json.loads(response.content)[0] 
        expected_camp = CampPage.objects.get(pk=camp['id'])
        image_url = get_expected_image_url(expected_camp.image.image.name, request)   
        expected_camp_data = {
            'id': expected_camp.pk,
            'camp_name' : expected_camp.get_name_display(),
            'description' : expected_camp.description,
            'camp_image' : image_url,
            'camp_leader' : None            
        }          
        self.assertDictEqual(camp, expected_camp_data)


class AboutUsLeadersTestCase(APITestCase):
    """
        about-us-organization_leaders

        # return only execomm (No directors/othr)
    """    
    @classmethod
    def setUpTestData(cls):
        cls.leaders_limit = 7 # Pres to overseer (execomm)
        cls.image_file = get_test_image_file()
        cls.request_factory = RequestFactory()
        positions = OrgLeader.Positions.labels
        positions.remove(OrgLeader.Positions.DIRECTOR.label)
        positions.remove(OrgLeader.Positions.OTHER.label)
        cls.expected_positions = positions

    def test_get_org_leaders(self):
        """
        - test endpoint 'about-us-organization-leaders'
        - test leader_limit
        mock: create 7 org leaders (execom [pres to overseer])
        """
        
        for _ in range (7):
            OrgLeader.objects.create(
                first_name = 'Extra',
                last_name = 'Leader',
                background = 'background',
                advocacy = 'advocacy',
                position = OrgLeader.Positions.values[_],
                image=Image.objects.create(name = 'other', image = self.image_file)
            )        

        response = self.client.get(reverse("about-us-organization-leaders"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)  
        self.assertLessEqual( len(response.data),  self.leaders_limit)  
    
    def test_get_execomm_leaders(self):
        """
        - test if all are execomm leaders
        mock: create 9 org leaders (execom [pres to overseer] + director + othr)
        """        
        for _ in range (9):
            OrgLeader.objects.create(
                first_name = 'Extra',
                last_name = 'Leader',
                background = 'background',
                advocacy = 'advocacy',
                position = OrgLeader.Positions.values[_],
                image=Image.objects.create(name = 'other', image = self.image_file)
            )             

        response = self.client.get(reverse("about-us-organization-leaders"))

        for leader in response.data:
            response_leader = OrgLeader.objects.get(pk=leader['leader_id'])
            self.assertNotIn(response_leader.position,  
                [OrgLeader.Positions.DIRECTOR.value,
                 OrgLeader.Positions.OTHER.value]
            ) 
 
    def test_get_execomm_leader_data(self):
        """
        - test expected execomm data
        mock: create 1 org leaders (Pres)
        """        
        OrgLeader.objects.create(
            first_name = 'Extra',
            last_name = 'Leader',
            background = 'background',
            advocacy = 'advocacy',
            position = OrgLeader.Positions.PRESIDENT,
            image=Image.objects.create(name = 'other', image = self.image_file)
        )             
        request = self.request_factory.get(reverse('about-us-organization-leaders'))
        response = self.client.get(reverse('about-us-organization-leaders'))

        response_leader = json.loads(response.content)[0] 
        expected_leader = OrgLeader.objects.get(pk=response_leader['leader_id'])
        image_url = get_expected_image_url(expected_leader.image.image.name, request)

        expected_leader_data = {
            'leader_id' : expected_leader.id,
            'image_url' : image_url
        }

        self.assertDictEqual(expected_leader_data, response_leader)
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

