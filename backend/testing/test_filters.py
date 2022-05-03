from rest_framework.test import APITestCase, APIRequestFactory
from kalunwa.content.models import(
    Event,
    Image,
)
from kalunwa.content.filters import(
    ExcludeIDFilter
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

    def test_expected_query_integer_input(self):
        # 0 -> returns 0 or no events
        query_limit = 0
        response = self.client.get(f'/api/events/?query_limit={query_limit}')        
        self.assertEqual(len(response.data), 0)
        # 3 -> returns 3 events
        query_limit = 3
        response = self.client.get(f'/api/events/?query_limit={query_limit}')        
        self.assertEqual(len(response.data), query_limit)        
        # 5 -> returns 5 events
        query_limit = 5
        response = self.client.get(f'/api/events/?query_limit={query_limit}')        
        self.assertEqual(len(response.data), query_limit)           
        # 6 -> returns 5 events
        query_limit = 6
        response = self.client.get(f'/api/events/?query_limit={query_limit}')        
        self.assertEqual(len(response.data), self.event_count)
        # aaa -> strings are ignored

    def test_negative_query_integer_input(self):
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
        # -1 -> ignores negative, return all events
        response = self.client.get(f'/api/events/')
        self.assertEqual(len(response.data), self.event_count)            

"""
Test QueryLimitBackend: Gallery

tests:
    - if no model -> error 
    - is used by a model that has no gallery 
""" 
# event, 
class ExcludeIDFilterTestCase(APITestCase):
    """
    mock viewset that uses this logic e.g. Event
    -> test on list endpoint
        - mock 5 events
        - an int 
            - id exists
                - filter to id
            - behavior if value does not exist 
                - filters none so ignore; return qs
        - a list of ints 
            - would not pass is_digit check so ignore
        - is negative
            - would not pass is_digit check so ignore
        - id__not is an integer ()
            - ignore, return original             
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
        cls.event_count = Event.objects.all().count()

    def test_id_exists_input(self):
        # id exists -> all except that id 
        excluded_id = Event.objects.first().id
        response = self.client.get(f'/api/events/?id__not={excluded_id}')   
        self.assertEqual(len(response.data), self.event_count - 1)
        for event in response.data:
            self.assertNotEqual(event['id'], excluded_id)

    def test_id_not_exist_input(self):
        # id does not exist -> return all 
        not_exist_id = self.event_count+1
        response = self.client.get(f'/api/events/?id__not={not_exist_id}')
        self.assertEqual(len(response.data), self.event_count)

    def test_list_of_id_input(self):
        # does not pass isdigit() check, return all
        response = self.client.get(f'/api/events/?id__not={1,2,3}')
        self.assertEqual(len(response.data), self.event_count)

    def test_negative_integer_input(self):
        # -1 -> ignores negative, return all events
        id = -1
        response = self.client.get(f'/api/events/?id__not={id}')
        self.assertEqual(len(response.data), self.event_count)

    def test_string_query_input(self):
        query_limits = ['aaa', '*&()', '']
        for query_limit in query_limits:
            response = self.client.get(f'/api/events/?query_limit={query_limit}')        
            self.assertEqual(len(response.data), self.event_count)  