import json
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase, APIRequestFactory
from kalunwa.content.serializers import StatusEnum
from .utils import  (
    ANNOUNCEMENT_LATEST_ONE,
    ABOUT_US_CAMP_URL, 
    ABOUT_US_LEADERS,
    ABOUT_US_TOTAL_MEMBERS, 
    CAMP_DETAIL_GALLERY_LIMIT,
    EVENT_DETAIL_CONTRIBUTORS,
    EVENT_DETAIL_GALLERY_LIMIT,
    HOMEPAGE_EVENT_URL,
    HOMEPAGE_JUMBOTRON_URL,     
    HOMEPAGE_NEWS_URL,
    HOMEPAGE_PROJECT_URL, 
    PROJECT_DETAIL_CONTRIBUTORS, 
    PROJECT_DETAIL_GALLERY_LIMIT, 
    get_expected_image_url, 
    get_test_image_file, 
    to_expected_iso_format,
    # to_formal_mdy, 
)
from kalunwa.content.models import(
    Announcement,
    CampEnum, 
    CampLeader, 
    CampPage, 
    Contributor, 
    Demographics,  
    Event,
    Image, 
    Jumbotron, 
    News, 
    OrgLeader, 
    Project,     
)
from rest_framework import status
#-------------------------------------------------------------------------------
# HomePage Website

class HomepageJumbotronsTestCase(APITestCase):
    """
    Test jumbotron endpoint for homepage (hp):
    tests:
        - test list endpoint (status ok) and limit (5)
        - test if featured jumbotrons are returned for hp
        - test expected jumbotron data for homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.jumbotron_limit = 5
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.url = HOMEPAGE_JUMBOTRON_URL
    
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
                image = Image.objects.create(name=f'image_{_}', image=self.image_file),  
                is_featured=True,                
            )

        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.jumbotron_limit) # a <= b

    def test_get_homepage_featured_jumbotrons(self):
        """
        Test if only featured jumbotrons are returned. 
        mock: 2 featured and 3 non-featured.
        """        
        for _ in range(5): 
            if _ == [0,1]: # first 2 events are featured, rest are not
                featured = True
            else:
                featured = False      

            Jumbotron.objects.create(
            header_title= f'Jumbotron {_}', 
            subtitle= f'short description {_}',
            image = Image.objects.create(name=f'image_{_}', image=self.image_file),
            is_featured=featured,
        )                     

        response = self.client.get(self.url) 
        jumbotrons = response.data       

        for jumbotron in jumbotrons:
            fetched_jumbotron = Event.objects.get(pk=jumbotron['id'])
            self.assertTrue(fetched_jumbotron.is_featured)         


    def test_get_homepage_jumbotron_data(self):
        """
        Given no variation with serializing jumbotron data, retrieving and 
        checking only 1 for its content is enough. 

        Assumption: Jumbotron object has the appropriate fields.  
        """
        expected_jumbotron = Jumbotron.objects.create(
            header_title= 'Jumbotron 1', 
            subtitle= 'short description',
            image = Image.objects.create(name=f'image_1', image=self.image_file),  
            is_featured=True,        
        )
        # need request to build image full url (request scheme, host)
        request = self.request_factory.get(self.url)
        response = self.client.get(self.url) 
        response_jumbotron = json.loads(response.content)[0] # json to python 
 

        image_url = get_expected_image_url(expected_jumbotron.image.image.name, request)
        
        expected_jumbotron_data = {
            'id' : expected_jumbotron.id, 
            'header_title' : expected_jumbotron.header_title,
            'subtitle' : expected_jumbotron.subtitle,
            'image' : {'image':image_url}
        }

        self.assertDictEqual(response_jumbotron, expected_jumbotron_data)


class HomepageEventsTestCase(APITestCase):
    """
    Test event endpoint for homepage (hp):
        - test list endpoint (status ok) and limit (3)    
        - test if featured events are returned for hp        
        - test expected events data for homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.event_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.url = HOMEPAGE_EVENT_URL
    
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

        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), self.event_limit) # a <= b

    def test_get_homepage_featured_events(self):
        """
        Test if only featured events are returned. 
        mock: 2 featured and 3 non-featured.
        """

        for _ in range(5): 
            if _ in [0,1]: # first 2 events are featured, rest are not
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

        response = self.client.get(self.url) 
        events = response.data

        for event in events:
            fetched_event = Event.objects.get(pk=event['id'])
            self.assertTrue(fetched_event.is_featured)
    
    def test_get_homepage_event_data(self):
        expected_event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )       

        request = self.request_factory.get(self.url)
        response = self.client.get(self.url) 
        
        event = json.loads(response.content)[0]
        image_url = get_expected_image_url(expected_event.image.image.name, request)

        expected_event_data = {
            'id' : expected_event.id,
            'title' : expected_event.title,
            'image' : { 'image' : image_url}
        } 
        self.assertDictEqual(event, expected_event_data)
    

class HomepageProjectsTestCase(APITestCase):
    """
    Test project endpoint for homepage (hp):
        - test list endpoint (status ok) and limit (3)    
        - test if featured projects are returned for hp        
        - test expected project data for homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.project_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.url = HOMEPAGE_PROJECT_URL
    
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

        
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual(len(response.data), self.project_limit) # a <= b

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

        response = self.client.get(self.url) 
        projects = response.data

        for project in projects:
            fetched_project = Project.objects.get(pk=project['id'])
            self.assertTrue(fetched_project.is_featured)
    
    def test_get_homepage_project_data(self):
        expected_project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )       

        request = self.request_factory.get(self.url)
        response = self.client.get(self.url) 
        
        project = json.loads(response.content)[0]
        image_url = get_expected_image_url(expected_project.image.image.name, request)

        expected_project_data = {
            'id' : expected_project.id,
            'title' : expected_project.title,
            'image' : {'image' : image_url}
        } 
        self.assertDictEqual(project, expected_project_data)


class HomepageNewsTestCase(APITestCase):
    """
    Test news endpoint for homepage (hp):
        - test list endpoint (status ok) and limit (3)    
        - test if latest news are returned for hp        
        - test expected news data for homepage
    """
    @classmethod
    def setUpTestData(cls):
        """
        - separate test for latest news,
        - separate test for limit
        """
        cls.news_limit = 3
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.url = HOMEPAGE_NEWS_URL

    def test_get_homepage_news(self):
        """
        Tests list endpoints for homepage news, return OK code. Tests list limit. 
        mock: create 4
        """
        # create 4 news
        for _ in range(4): 
            News.objects.create(
            title= f'News {_}', 
            description= f'description {_}',
            image = Image.objects.create( name=f'image_{_}', image=self.image_file)               
            )   

        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual(len(response.data), self.news_limit) # a <= b

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

        response = self.client.get(self.url) 
        news_set = response.data

        pk = 4
        for news in news_set:
            self.assertEqual(news['id'], pk) # error here
            pk-=1
  
    def test_get_homepage_news_data(self):
        expected_news = News.objects.create(
        title= 'News 1', 
        description= 'description 1',
        image = Image.objects.create(name='image_1', image=self.image_file),
        )   

        request = self.request_factory.get(self.url)
        response = self.client.get(self.url) 
        
        news = json.loads(response.content)[0]
        image_url = get_expected_image_url(expected_news.image.image.name, request)

        expected_news_data = {
            'id' : expected_news.id,
            'title' : expected_news.title,
            'description' : expected_news.description,
            'image' : {'image' : image_url}
        } 
        self.assertDictEqual(news, expected_news_data)

#-------------------------------------------------------------------------------
# About Us Website

class AboutUsDemographicsTestCase(APITestCase):
    """
    Test demographics endpoints for about us:    
    tests:
        - test list endpoint (status ok)     
        - test if total is correct          
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
        cls.request_factory = APIRequestFactory()    
        cls.url = ABOUT_US_TOTAL_MEMBERS # or reverse("demographics-total-members")

    def test_get_demographics(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)    

    def test_get_demographics_data(self):
        response = self.client.get(self.url)  
        self.assertEqual(response.data['total_members'], self.total_members)


class AboutUsCampsTestCase(APITestCase):
    """
    Test camps endpoints for about us:    
        - test camp endpoint (status ok), return all camps 
        - test if expected camp types are retrieved (SUba, Baybayon, Lasang, Zero Waste)     
        - test expected news data for homepage

        # tried testing for getting duplicate camps
            # not possible, since  the unique constraint stops model creation
            #  with the same name    
        # possible additions:
            # more than 1 camp leaders -> make campleader an fk nlng kaya 
            # no test if 3 camps, lacking 1; what is the expected behavior            
    """    

    @classmethod
    def setUpTestData(cls):    
        cls.camp_count = 4
        cls.image_file = get_test_image_file()
        cls.expected_camps = CampEnum.labels
        cls.expected_camps.remove(CampEnum.GENERAL.label)
        cls.request_factory = APIRequestFactory() 
        cls.url = ABOUT_US_CAMP_URL       

    def test_get_camps(self):
        """
        - test camp endpoint (status ok), return camps 
        - test if expected camp types are retrieved (Suba, Baybayon, Lasang, Zero Waste)
        - test expected camp data 
        mock: 5 camps (expected + general)     
        """

        for _ in range(4):
            # camp pages    
            CampPage.objects.create(
                name=CampEnum.values[_],
                description = 'default description',
                image = Image.objects.create(name = 'name', image = self.image_file)
        )   
        response = self.client.get(self.url)
        response_camps = []
        for camp in response.data:
            response_camps.append(camp['name']) 

        self.assertEqual(status.HTTP_200_OK, response.status_code)  
        self.assertEqual( self.camp_count, len(response.data))   
        self.assertListEqual(sorted(self.expected_camps), sorted(response_camps))

    def test_get_camp_data(self):
        expected_camp = CampPage.objects.create(
            name=CampEnum.SUBA.value,
            description='default',
            image = Image.objects.create(name = 'name', image = self.image_file)            
        )        

        expected_leader = CampLeader.objects.create(
            first_name='Suba leader',
            last_name = 'Suba last n',
            quote='spread wings',
            image = Image.objects.create(name = 'name', image = self.image_file),
            camp = CampEnum.SUBA.value,
            position = CampLeader.Positions.LEADER,
            motto = 'all is well'
        )
        request = self.request_factory.get(self.url)
        response = self.client.get(self.url)  

        camp = json.loads(response.content)[0] 
        camp_image_url = get_expected_image_url(expected_camp.image.image.name, request)   
        leader_image_url = get_expected_image_url(expected_leader.image.image.name, request)           
        expected_camp_data = {
            'id': expected_camp.pk,
            'name' : expected_camp.get_name_display(),
            'description' : expected_camp.description,
            'tagline' : expected_camp.tagline,
            'image' : {
                'id' : expected_camp.image.pk,
                'image' : camp_image_url,
            },
            'camp_leader' : { 
                'id': expected_leader.id, 
                'name': expected_leader.get_fullname(),
                'motto' : expected_leader.motto,
                'image' : {
                    'id' : 2,
                    'image': leader_image_url,
                }

            }            
        }   
        self.assertDictEqual(camp, expected_camp_data)


class AboutUsLeadersTestCase(APITestCase):
    """
        - test if retrieved leaders are part of the execomm
        - test expected leader data
    """    
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.execomm_positions = [position for position in OrgLeader.Positions.values
                            if position not in [OrgLeader.Positions.DIRECTOR.value, 
                                                OrgLeader.Positions.OTHER.value]] ## change to label soon
        cls.url = ABOUT_US_LEADERS

    def test_get_org_leaders(self):
        """
        - test if leaders are part of the execomm
        mock: create 9 org leaders (execom [pres to overseer] + director & other)
        """
        for _ in range (9):
            OrgLeader.objects.create(
                first_name = 'Extra',
                last_name = 'Leader',
                quote = 'advocacy',
                position = OrgLeader.Positions.values[_],
                image=Image.objects.create(name = 'other', image = self.image_file)
            )        
        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code) 
        self.assertEqual(len(response.data), 7) 

        for leader in response.data:
            response_leader = OrgLeader.objects.get(pk=leader['id'])
            self.assertIn(response_leader.position, self.execomm_positions)     
 
    def test_get_execomm_leader_data(self):
        """
        - test expected execomm data
        mock: create 1 org leaders (Pres)
        """        
        expected_leader = OrgLeader.objects.create(
            first_name = 'Extra',
            last_name = 'Leader',
            quote = 'background',
            position = OrgLeader.Positions.PRESIDENT,
            image=Image.objects.create(name = 'other', image = self.image_file)
        )             
        request = self.request_factory.get(self.url)
        response = self.client.get(self.url)

        response_leader = json.loads(response.content)[0] 
        image_url = get_expected_image_url(expected_leader.image.image.name, request)
        expected_leader_data = {
            'id' : expected_leader.id,
            'image' : {
                'id' : 1,
                'image' : image_url
                }
        }
        self.assertDictEqual(expected_leader_data, response_leader)      


# ------------------------------------------------------------------------------
# website list and views

class EventGetTestCase(APITestCase):
    """
    tests the get method for list and detail endpoints.
        - test event list endpoint (status ok), return created events
        - test event detail endpoint (status ok), return created event
        - test event detail response data
        - test event endpoint (status ok) with expanded gallery
        - test event gallery limit
        - test event gallery response data
        - test event endpoint (status ok) with expanded contributors
        - test event contributor response data     
    
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_get_event_list(self):
        """
        - test event list endpoint (status ok), return created events
        """
        for _ in range(5): 
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file),  
            is_featured=True,
            )           
        response = self.client.get(reverse('event-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), 5)    

    def test_get_event_detail(self):
        """
        - test event detail endpoint (status ok), return created event
        - test event detail response data
        """        
        expected_event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )       

        response = self.client.get(reverse('event-detail', args=[1]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        response_event = response.data
        expected_event_data = {
            'id': expected_event.id,
            'title': expected_event.title,
            'image': expected_event.image.pk, 
            'description' : expected_event.description,
            'start_date' : to_expected_iso_format(expected_event.start_date),
            'end_date' : to_expected_iso_format(expected_event.end_date),
            'camp' : expected_event.get_camp_display(),
            'created_at': to_expected_iso_format(expected_event.created_at),
            'updated_at': to_expected_iso_format(expected_event.updated_at),
            'status': StatusEnum.PAST.value # based on dates set
        }
        self.assertDictEqual(expected_event_data, response_event)
  
    def test_get_event_gallery(self):
        """
        - test event endpoint (status ok) with expanded gallery
        - test event gallery limit        

        mock :
            1 event related to 11 diff images
        
        """
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )     
#############
            # Event.objects.create(
            #     title= f'Event {_}', 
            #     description= f'description {_}',
            #     start_date=timezone.now(),
            #     end_date=timezone.now(),
            #     image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            # ) 
#############
        for _ in range(11):
            Image.objects.create(name='image_1', image=self.image_file)
        
        event.gallery.set(Image.objects.all().values_list('id', flat=True))
        response = self.client.get(EVENT_DETAIL_GALLERY_LIMIT)
        gallery = response.data[0]['gallery']
        self.assertEqual(status.HTTP_200_OK, response.status_code)                
        self.assertLessEqual(len(gallery), 10)           

    def test_get_event_gallery_data(self):
        """
        - test event gallery response data        
        data:
            id, image_url        
        """        
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )     
        image = Image.objects.get(pk=1) 
        event.gallery.add(image)               

        request = self.request_factory.get(EVENT_DETAIL_GALLERY_LIMIT)
        response = self.client.get(EVENT_DETAIL_GALLERY_LIMIT)
        gallery = json.loads(response.content)[0]['gallery']

        expected_gallery_data = {
            'id':image.id,
            'image': get_expected_image_url(image.image.name, request)
        } 
        self.assertDictEqual(gallery[0], expected_gallery_data)
    
    def test_get_event_contributors(self):
        """
        - test event endpoint (status ok) with expanded contributors
        - test returned contributors
        mock :
            1 event related to 5 contributors
        
        """
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )   
        for _ in range(5):        
            Contributor.objects.create(
            name= 'Contributor 1', 
            category= Contributor.Categories.SPONSOR,
            image = Image.objects.create(name='image_1', image=self.image_file),
        )     
        event.contributors.set(Contributor.objects.all().values_list('id', flat=True))
        response = self.client.get(EVENT_DETAIL_CONTRIBUTORS)
        contributors = response.data[0]['contributors']
        self.assertEqual(status.HTTP_200_OK, response.status_code)        
        self.assertEqual(len(contributors), 5)           

    def test_get_event_contributors_data(self):
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )     
        expected_contributor  = Contributor.objects.create(
            name= 'Contributor 1', 
            category= Contributor.Categories.SPONSOR,
            image = Image.objects.create(name='image_1', image=self.image_file),
        )
        event.contributors.add(expected_contributor)               
        request = self.request_factory.get(EVENT_DETAIL_CONTRIBUTORS)
        response = self.client.get(EVENT_DETAIL_CONTRIBUTORS)
        response_contributor = json.loads(response.content)[0]['contributors']
        expected_contributor_data = {
            'id':expected_contributor.id,
            'name': expected_contributor.name,
            'image': {
                'id': expected_contributor.image.id,
                'image': get_expected_image_url(expected_contributor.image.image.name, request)
            },
            'category' : expected_contributor.category.label
        } 
        self.assertDictEqual(response_contributor[0], expected_contributor_data)
        

class ProjectGetTestCase(APITestCase):
    """
    tests the get method for list and detail endpoints.
        - test project list endpoint (status ok), return created projects
        - test project detail endpoint (status ok), return created project
        - test project detail response data
        - test project endpoint (status ok) with expanded gallery, return gallery images
        - test project gallery limit
        - test project gallery response data
        - test project endpoint (status ok) with expanded contributors, return contributors
        - test project contributor response data   
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_get_project_list(self):
        """
        - test project list endpoint (status ok), return created projects        
        """
        for _ in range(5): 
            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file),  
            is_featured=True,
            )           

        response = self.client.get(reverse('project-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), 5)        

    def test_get_project_detail(self):
        """
        - test project detail endpoint (status ok), return created project
        - test project detail response data       
        """
        expected_project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )       

        response = self.client.get(reverse('project-detail', args=[1]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        response_project = response.data

        expected_project_data = {
            'id': expected_project.id,
            'title': expected_project.title,
            'image': expected_project.image.pk, 
            'description' : expected_project.description,
            'start_date' : to_expected_iso_format(expected_project.start_date),
            'end_date' : to_expected_iso_format(expected_project.end_date),
            'camp' : expected_project.get_camp_display(),
            'created_at': to_expected_iso_format(expected_project.created_at),
            'updated_at': to_expected_iso_format(expected_project.updated_at),
            'status': StatusEnum.PAST.value # based on dates set
        }
        self.assertDictEqual(expected_project_data, response_project)

    def test_get_project_gallery(self):
        """
        - test project endpoint (status ok) with expanded gallery, return gallery images
        - test project gallery limit (10)
        mock :
            1 project related to 11 diff images
        
        """
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )    

        for _ in range(11):
            Image.objects.create(name='image_1', image=self.image_file)
        
        project.gallery.set(Image.objects.all().values_list('id', flat=True))
        response = self.client.get(PROJECT_DETAIL_GALLERY_LIMIT)
        self.assertEqual(status.HTTP_200_OK, response.status_code)        
        
        gallery = response.data[0]['gallery']
        self.assertEqual( len(gallery), 10)           

    def test_get_project_gallery_data(self):
        """
        - test project gallery response data        
        data:
            id, image_url
        """        
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )     
        image = Image.objects.get(pk=1) 
        project.gallery.add(image)               

        request = self.request_factory.get(PROJECT_DETAIL_GALLERY_LIMIT)
        response = self.client.get(PROJECT_DETAIL_GALLERY_LIMIT)
        gallery = json.loads(response.content)[0]['gallery']

        expected_gallery_data = {
            'id':image.id,
            'image': get_expected_image_url(image.image.name, request)
        } 
        self.assertDictEqual(gallery[0], expected_gallery_data)
    
    def test_get_project_contributors(self):
        """
        - test project endpoint (status ok) with expanded contributors, return contributors
        mock :
            1 project related to 5 contributors
        
        """
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )    
        for _ in range(5):        
            Contributor.objects.create(
            name= 'Contributor 1', 
            category= Contributor.Categories.SPONSOR,
            image = Image.objects.create(name='image_1', image=self.image_file),
        )     
        project.contributors.set(Contributor.objects.all().values_list('id', flat=True))
        response = self.client.get(PROJECT_DETAIL_CONTRIBUTORS)
        self.assertEqual(status.HTTP_200_OK, response.status_code)        
        contributors = response.data[0]['contributors']
        self.assertLessEqual( len(contributors), 5)           

    def test_get_project_contributors_data(self):
        """
        - test project contributor response data        
        """        
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
            is_featured=True,
        )  
        expected_contributor = Contributor.objects.create(
            name= 'Contributor 1', 
            category= Contributor.Categories.SPONSOR,
            image = Image.objects.create(name='image_1', image=self.image_file),
        )
        project.contributors.add(expected_contributor)               
        request = self.request_factory.get(PROJECT_DETAIL_CONTRIBUTORS)
        response = self.client.get(PROJECT_DETAIL_CONTRIBUTORS)
        response_contributor = json.loads(response.content)[0]['contributors']
        expected_contributor_data = {
            'id':expected_contributor.id,
            'name': expected_contributor.name,
            'image': {
                'id': expected_contributor.image.id,
                'image': get_expected_image_url(expected_contributor.image.image.name, request)
            },
            'category' : expected_contributor.category.label
        } 
        self.assertDictEqual(response_contributor[0], expected_contributor_data)


class CampGetTestCase(APITestCase):
    """
    tests the get method for list and detail endpoints.
        - test camp list endpoint (status ok), return created events
        - test camp detail endpoint (status ok), return created camp
        - test camp detail response data
        - test camp endpoint (status ok) with expanded gallery
        - test camp gallery limit
        - test camp gallery response data
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_get_camp_list(self):
        """
        - test project list endpoint (status ok), return created projects                
        """
        
        for _ in range(5):
            CampPage.objects.create(
                name=CampEnum.values[_],
                description = 'default description',
                tagline = 'tagline',
                image = Image.objects.create(name = 'name', image = self.image_file)
            )            

        response = self.client.get(reverse('camp-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertLessEqual( len(response.data), 5)

    def test_camp_detail(self):
        """
        - test camp detail endpoint (status ok), return created camp            
        """    
        expected_camp = CampPage.objects.create(
            name=CampEnum.GENERAL.value,
            description = 'default description',
            tagline = 'tagline',
            image = Image.objects.create(name = 'name', image = self.image_file)
        )        

        response = self.client.get(reverse('camp-detail', args=[1]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response_camp = response.data

        expected_camp_data = {
            'id' : expected_camp.id,
            'name': CampEnum.GENERAL.label,
            'description': expected_camp.description,
            'tagline': expected_camp.tagline,
            'image' : expected_camp.image.pk, 
            'camp_leader': None,
            'created_at': to_expected_iso_format(expected_camp.created_at),
            'updated_at': to_expected_iso_format(expected_camp.updated_at)
        }
        self.assertDictEqual(expected_camp_data, response_camp)
        
    def test_get_camp_gallery(self):
        """
        - test camp endpoint (status ok) with expanded gallery, return gallery images
        - test camp gallery limit (10)
        mock :
            1 project related to 11 diff images
        
        """
        camp = CampPage.objects.create(
            name=CampEnum.GENERAL.value,
            description = 'default description',
            tagline = 'tagline',
            image = Image.objects.create(name = 'name', image = self.image_file)
        )    

        for _ in range(11):
            Image.objects.create(name='image_1', image=self.image_file)
        
        camp.gallery.set(Image.objects.all().values_list('id', flat=True))
        response = self.client.get(CAMP_DETAIL_GALLERY_LIMIT)
        self.assertEqual(status.HTTP_200_OK, response.status_code)        
        
        gallery = response.data[0]['gallery']
        self.assertEqual( len(gallery), 10)   

    def test_get_project_gallery_data(self):
        """
        - test camp gallery response data        
        data:
            id, image_url
        """
        camp = CampPage.objects.create(
            name=CampEnum.GENERAL.value,
            description = 'default description',
            tagline = 'tagline',
            image = Image.objects.create(name = 'name', image = self.image_file)
        )    
        image = Image.objects.get(pk=1) 
        camp.gallery.add(image)               

        request = self.request_factory.get(CAMP_DETAIL_GALLERY_LIMIT)
        response = self.client.get(CAMP_DETAIL_GALLERY_LIMIT)
        gallery = json.loads(response.content)[0]['gallery']

        expected_gallery_data = {
            'id':image.id,
            'image': get_expected_image_url(image.image.name, request)
        } 
        self.assertDictEqual(gallery[0], expected_gallery_data)   


class AnnouncementGetTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:    
        cls.request_factory = APIRequestFactory()

    def test_get_announcement_list(self):
        """
            - test announcement endpoint (status ok), return created announcements    
        """        
        for _ in range(5):
            Announcement.objects.create(
                title='announcement',
                description = 'description'
            )
        response = self.client.get(reverse('announcement-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual( len(response.data), 5)       

    def test_get_announcement_detail(self):
        """
            - test announcement detail endpoint (status ok), return created announcement   
        """        
        expected_announcement = Announcement.objects.create(
                title='announcement',
                meta_description = 'meta_description',                
                description = 'description'
        )
        response = self.client.get(reverse('announcement-detail', args=[1]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response_announcement = json.loads(response.content)
        expected_announcement_data = {
            'id': expected_announcement.id,
            'title': expected_announcement.title,
            'meta_description' : expected_announcement.meta_description,              
            'description' : expected_announcement.description,      
            'created_at': to_expected_iso_format(expected_announcement.created_at), 
            'updated_at': to_expected_iso_format(expected_announcement.updated_at),                      
        }
        self.assertDictEqual(expected_announcement_data, response_announcement)        

        
class AnnouncementLatestTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:    
        cls.request_factory = APIRequestFactory()
        cls.url = ANNOUNCEMENT_LATEST_ONE

    def test_get_latest_announcement(self):      
        for _ in range(5):
            Announcement.objects.create(
                title='announcement',
                meta_description = 'meta_description',
                description = 'description'
            )

        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_announcement = Announcement.objects.first() # ordered by latest
        response_announcement = json.loads(response.content)[0]
        latest_announcement_data = {
            'id': expected_announcement.id,
            'title': expected_announcement.title,
            'meta_description' : expected_announcement.meta_description,             
            'description' : expected_announcement.description,                
        }        
        self.assertDictEqual(latest_announcement_data, response_announcement)
            

class NewsGetTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:    
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_get_news_list(self):
        """
            - test news endpoint (status ok), return created news  
        """        
        for _ in range(5):
            News.objects.create(
                title='news {_}',
                description = 'description',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file)
            )
        response = self.client.get(reverse('news-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual( len(response.data), 5)       

    def test_get_news_detail(self):
        """
            - test news detail endpoint (status ok), return created news  
        """        
        expected_news = News.objects.create(
                title='news',                
                description = 'description',
                image = Image.objects.create(name='image_1', image=self.image_file)
        )

        response = self.client.get(reverse('news-detail', args=[1]))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response_news = response.data

        expected_news_data = {
            'id': expected_news.id,
            'title': expected_news.title,           
            'description' : expected_news.description,    
            'image': expected_news.image.pk,       
            'created_at': to_expected_iso_format(expected_news.created_at), 
            'updated_at': to_expected_iso_format(expected_news.updated_at),                      
        }

        self.assertDictEqual(expected_news_data, response_news)        

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
        
    # def test_news_validation_post(self):
    #     response = self.client.post(reverse('news-list'))

