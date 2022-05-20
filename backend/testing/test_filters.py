from rest_framework.test import APITestCase
from kalunwa.content.models import(
    CabinOfficer,
    CampEnum,
    CampLeader,
    CampPage,
    Commissioner,
    Event,
    Image,
    News,
    OrgLeader,
)
from .utils import (
    get_test_image_file,
)
from django.utils import timezone


class QueryLimitTestCase(APITestCase):
    """
    mock viewset that uses this logic e.g. Event
    -> test on list endpoint
        - mock 5 events
        - query limit is an integer.
        - query limit values to test: [-1, 0, 3, 5, 6]
            # negative value
            # zero
            # less than total events
            # exact no. of events
            # greater than no. of events
            # strings
                # empty string
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(5): 
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            is_featured=True,
            )           

        cls.event_count = len(Event.objects.all())            

    def test_expected_integer_zero_input(self):
        # 0 -> returns 0 or no events
        response = self.client.get(f'/api/events/?query_limit={0}')        
        self.assertEqual(len(response.data), 0)

    def test_expected_integer_less_than_count(self):         
        #  (test less than)
        response = self.client.get(f'/api/events/?query_limit={self.event_count-1}')        
        self.assertEqual(len(response.data), self.event_count-1)        

    def test_expected_integer_equal_count(self):    
        #  (test exact)
        response = self.client.get(f'/api/events/?query_limit={self.event_count}')        
        self.assertEqual(len(response.data), self.event_count)           

    def test_expected_integer_greater_than_count(self):     
        # (test greater than)
        response = self.client.get(f'/api/events/?query_limit={self.event_count+1}')        
        self.assertEqual(len(response.data), self.event_count)

    def test_expected_integer_equal_count(self):  
        # -1 -> ignores negative, return all events
        query_limit = -1
        response = self.client.get(f'/api/events/?query_limit={query_limit}')
        self.assertEqual(len(response.data), self.event_count)

    def test_string_query_input(self):
        query_limits = ['aaa', '*&()', '']

        for query_limit in query_limits:
            response = self.client.get(f'/api/events/?query_limit={query_limit}')        
            self.assertEqual(len(response.data), self.event_count)   

    def test_no_query_limit_param(self): # default to None
        response = self.client.get(f'/api/events/')
        self.assertEqual(len(response.data), self.event_count)     


class QueryLimitGalleryTestCase(APITestCase):
    """
    assumptions:
    - viewset has a model attribute (custom defined)
    - used by a viewset, to which its model has a related gallery
        - related name should be 'gallery_<content>s' e.g. gallery_events
    - these assumptions are made, because errors from these are programmer-driven
    and not user/client driven
    
    mock : 
        - viewset that uses this logic e.g. Event    
        - mock 5 events        
    tests:
    - limit is a valid number
    - limit is 0 
    - limit is not a digit
    - limit is negative
    - limit is strings
    - test for list and detail (valid int input for both cases)
    - limit is None    
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        cls.event = Event.objects.create(
            title= f'Event 1', 
            description= f'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image', image=cls.image_file),  
            is_featured=True,
        )   
        for _ in range(3): 
            Image.objects.create(name=f'image', image=cls.image_file)
        cls.event.gallery.set(Image.objects.all())
        cls.gallery_count = len(cls.event.gallery.all())# one is merely a featured image  

    def test_expected_integer_zero_input(self):
        # 0 -> returns 0 or no events
            # list   
        gallery_limit = 0
        response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')   
        event = response.data[0]     
        self.assertEqual(len(event['gallery']), 0)
            # detail
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')                
        self.assertEqual(len(response.data['gallery']), 0) 

    def test_expected_integer_less_than_count(self):           
        # (test less than)
        gallery_limit = self.gallery_count-1      
            # list      
        response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')
        event = response.data[0]  
        self.assertEqual(len(event['gallery']), self.gallery_count-1) 
            # detail
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')                
        self.assertEqual(len(response.data['gallery']), self.gallery_count-1)  

    def test_expected_integer_equal_count(self):                 
        # (test exact)
        gallery_limit = self.gallery_count   
            # list        
        response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')
        event = response.data[0]  
        self.assertEqual(len(event['gallery']), self.gallery_count)  
            # detail       
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')             
        self.assertEqual(len(response.data['gallery']), self.gallery_count)    
         
    def test_expected_integer_greater_than_count(self):                   
        # (test greater than)
        gallery_limit = self.gallery_count+1        
            # list
        response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')
        event = response.data[0]  
        self.assertEqual(len(event['gallery']), self.gallery_count)  
            # detail 
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')                
        self.assertEqual(len(response.data['gallery']), self.gallery_count)                 

    def test_negative_integer_input(self):
        # -1 -> ignores negative, return all events
            # list 
        gallery_limit = -1
        response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')
        event = response.data[0]  
        self.assertEqual(len(event['gallery']), self.gallery_count)   
            # detail     
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')  
        self.assertEqual(len(response.data['gallery']), self.gallery_count)           

    def test_string_query_input(self):
        gallery_limits = ['aaa', '*&()', '']

        for gallery_limit in gallery_limits:
            #list 
            response = self.client.get(f'/api/events/?expand=gallery&query_limit_gallery={gallery_limit}')   
            event = response.data[0]       
            self.assertEqual(len(event['gallery']), self.gallery_count)   
            # detail
            response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery&query_limit_gallery={gallery_limit}')   
            self.assertEqual(len(response.data['gallery']), self.gallery_count)   

    def test_no_query_limit_param(self): # default to None
        # list
        response = self.client.get(f'/api/events/?expand=gallery')
        event = response.data[0]       
        self.assertEqual(len(event['gallery']), self.gallery_count)   
        # detail
        response = self.client.get(f'/api/events/{self.event.id}/?expand=gallery')           
        self.assertEqual(len(response.data['gallery']), self.gallery_count)   


class CampNameInFilterTestcase(APITestCase):
    """
    CampNameInFilterTest
    tests 
        - no filter on param
        - expected use case 
            'Suba,Baybayon,Lasang,Zero%20Waste'
        - 'Subba' 
            - returns empty list
        - correct labels but with many commas
            - would still work

    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()
        camp_values = CampEnum.values
        cls.expected_camp_labels = CampEnum.labels
        cls.expected_camp_labels.remove(CampEnum.GENERAL.label)

        # mock all including GENERAL
        for _ in range(5):

            CampPage.objects.create(
                name=camp_values[_],
                description = 'default description',
                image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            )

    def test_no_param(self): 
        response = self.client.get(f'/api/camps/')
        for camp in response.data:
            self.assertIn(camp['name'], CampEnum.labels)
    
    def test_expected_camps(self):
        response = self.client.get(f'/api/camps/?name__in=Suba,Baybayon,Lasang,Zero%20Waste')
        self.assertEqual(len(response.data), 4)
        for camp in response.data:
            self.assertIn(camp['name'], self.expected_camp_labels)   

    def test_not_valid_camp_single(self):
        # Subba -> returns empty list; qs filtering with an empty list -> .filter(name__in=[])
        response = self.client.get(f'/api/camps/?name__in=Subba')
        self.assertEqual(len(response.data), 0)        

    def test_not_valid_camp_with_valids(self):
        # ignores the invalid camp;
        response = self.client.get(f'/api/camps/?name__in=Subba,Baybayon,Lasang')
        self.assertEqual(len(response.data), 2)        
        for camp in response.data:
            self.assertIn(camp['name'], [CampEnum.BAYBAYON.label, CampEnum.LASANG.label])           

    def test_expected_camps_with_many_commas(self):
        response = self.client.get(f'/api/camps/?name__in=Suba,,,Baybayon,Lasang,,,,,Zero%20Waste')
        self.assertEqual(len(response.data), 4)
        for camp in response.data:
            self.assertIn(camp['name'], self.expected_camp_labels)   


class ExcludeIDFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()    
        for _ in range(3):
            image = Image.objects.create(name=f'image', image=cls.image_file)            
            News.objects.create(
            title= f'News {_}', 
            description= f'description {_}',
            image = image              
            )  
    
        cls.news_count = News.objects.count()

    def test_id_exists(self):
        # return all except the flagged id 
        expected_news = News.objects.last()
        response = self.client.get(f'/api/news/?id__not={expected_news.id}')
        self.assertEqual(self.news_count-1, len(response.data))
        for news in response.data:
            self.assertNotEqual(news['id'],expected_news.id)

    def test_id_doesnt_exist(self):
        # return all news
        response = self.client.get(f'/api/news/?id__not={self.news_count+1}')       
        self.assertEqual(self.news_count, len(response.data))       
                
    def test_id_is_invalid(self):
        # does not satisfy the isdigit check
        #return all news
        invalid_ids = ['aaa', '*&()', '']
        for invalid_id in invalid_ids:
            response = self.client.get(f'/api/news/?id__not={invalid_id}')                   
            self.assertEqual(self.news_count, len(response.data))             

    def test_no_id_not_param(self):
        response = self.client.get(f'/api/news/')                   
        self.assertEqual(self.news_count, len(response.data))    


class OrgLeaderPositionFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(9): 
            OrgLeader.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            position = OrgLeader.Positions.values[_]
            )           

        cls.orgleaders_count = len(OrgLeader.objects.all())   

    def test_correct_position_input(self): #all positions tested
        positions = ['President','Vice-President','Secretary','Treasurer','Auditor', 'Public Information Officer', 'Overseer', 'Director','Other']
        for position in positions:
            response = self.client.get(f'/api/orgleaders/?position={position}')       
            self.assertEqual(len(response.data), 1) 
    def test_execomm_position_input(self):
        position = 'ExeComm'
        response = self.client.get(f'/api/orgleaders/?position={position}')        
        self.assertEqual(len(response.data), 7)  
    def test_none_position_value_input(self):
        positions = [0, 'aaa', '@!*']
        for position in positions:
            response = self.client.get(f'/api/orgleaders/?position={position}')    
            self.assertEqual(len(response.data), 0) 
    def test_none_position_input(self):
        response = self.client.get(f'/api/orgleaders/?')       
        self.assertEqual(len(response.data), self.orgleaders_count)  


class CampLeaderPositionFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(3): 
            CampLeader.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            camp = CampEnum.values[_],
            position = CampLeader.Positions.values[_],
            motto = f'motto {_}'
            )           

        cls.campleader_count = len(CampLeader.objects.all())  

    def test_correct_position_input(self): #all positions tested
        positions = ['Camp Leader','Assistant Camp Leader','Other']
        for position in positions:
            response = self.client.get(f'/api/campleaders/?position={position}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_position_value_input(self):
        positions = [0, 'aaa', '@!*']
        for position in positions:
            response = self.client.get(f'/api/campleaders/?position={position}')    
            self.assertEqual(len(response.data), 0) 
    def test_none_position_input(self):
        response = self.client.get(f'/api/campleaders/?')       
        self.assertEqual(len(response.data), self.campleader_count) 


class CampFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(3): 
            CampLeader.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            camp = CampEnum.values[_],
            position = CampLeader.Positions.values[_],
            motto = f'motto {_}'
            )           

        cls.campleader_count = len(CampLeader.objects.all())   

    def test_correct_camp_input(self): #not all camps were tested since position index will be out of range
        camps = ['Suba','Lasang','Baybayon']
        for camp in camps:
            response = self.client.get(f'/api/campleaders/?camp={camp}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_camp_value_input(self):
        camps = [0, 'aaa', '@!*']
        for camp in camps:
            response = self.client.get(f'/api/campleaders/?camp={camp}')      
            self.assertEqual(len(response.data), 0) 
    def test_none_camp_input(self):
        response = self.client.get(f'/api/campleaders/?')       
        self.assertEqual(len(response.data), self.campleader_count)  


class CabinOfficerCategoryFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(4): 
            CabinOfficer.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            camp = CampEnum.values[_],
            category = CabinOfficer.Categories.values[_],
            position = CabinOfficer.Positions.values[_]
            )           

        cls.cabinofficer_count = len(CabinOfficer.objects.all())   

    def test_correct_category_input(self): #not all categories were tested since position index will be out of range
        categories = ['Secretariat Cabin','Finance Cabin','Ways and Means Cabin','Publicity Cabin']
        for category in categories:
            response = self.client.get(f'/api/cabinofficers/?category={category}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_category_value_input(self):
        categories = [0, 'aaa', '@!*']
        for category in categories:
            response = self.client.get(f'/api/cabinofficers/?category={category}')       
            self.assertEqual(len(response.data), 0) 
    def test_none_category_input(self):
        response = self.client.get(f'/api/cabinofficers/?')       
        self.assertEqual(len(response.data), self.cabinofficer_count)  


class CommissionerCategoryFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(3): 
            Commissioner.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            category = Commissioner.Categories.values[_],
            position = Commissioner.Positions.values[_]
            )           

        cls.commissioner_count = len(Commissioner.objects.all())   

    def test_correct_category_input(self): #all category tested
        categories = ['Election','Grievance and Ethics','Other']
        for category in categories:
            response = self.client.get(f'/api/commissioners/?category={category}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_category_value_input(self):
        categories = [0, 'aaa', '@!*']
        for category in categories:
            response = self.client.get(f'/api/commissioners/?category={category}')       
            self.assertEqual(len(response.data), 0)  
    def test_none_category_input(self):
        response = self.client.get(f'/api/commissioners/?')       
        self.assertEqual(len(response.data), self.commissioner_count)  

