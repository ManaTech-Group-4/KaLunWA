from rest_framework.test import APITestCase
from kalunwa.content.models import(
    CampEnum,
    CampPage,
    Event,
    Image,
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

            Event.objects.create(
                title= f'Event', 
                description= f'description',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = image,  
                is_featured=True,
            )   
        cls.event_count = Event.objects.count()

    def test_id_exists(self):
        # return all except the flagged id 
        expected_event = Event.objects.last()
        response = self.client.get(f'/api/events/?id__not={expected_event.id}')
        self.assertEqual(self.event_count-1, len(response.data))
        for event in response.data:
            self.assertNotEqual(event['id'],expected_event.id)

    def test_id_doesnt_exist(self):
        # return all events
        response = self.client.get(f'/api/events/?id__not={self.event_count+1}')       
        self.assertEqual(self.event_count, len(response.data))       
                
    def test_id_is_invalid(self):
        # does not satisfy the isdigit check
        #return all events
        invalid_ids = ['aaa', '*&()', '']
        for invalid_id in invalid_ids:
            response = self.client.get(f'/api/events/?id__not={invalid_id}')                   
            self.assertEqual(self.event_count, len(response.data))             

    def test_no_id_not_param(self):
        response = self.client.get(f'/api/events/')                   
        self.assertEqual(self.event_count, len(response.data))    