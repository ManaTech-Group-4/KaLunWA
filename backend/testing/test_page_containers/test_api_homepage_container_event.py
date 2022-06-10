import json
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from kalunwa.content.serializers import StatusEnum
from testing.utils import  (
    HOMEPAGE_EXPANDED_JUMBO_DETAIL_URL,
    get_test_image_file,
    get_expected_image_url,
    reverse_with_query_params,
    to_expected_iso_format,    
)
from kalunwa.content.models import(
    Event,
    Image,  
    
)
from kalunwa.page_containers.views import (
    PageContainerDetailView,
)
from kalunwa.page_containers.models import (
    PageContainer,
    PageContainedEvent,
)


class GetHomepageContainerEventsTestCase(APITestCase): 
    """
    # test get page_contained_events from homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.view = PageContainerDetailView.as_view()

    # api/page-containers/homepage/
    def test_get_homepage_events(self):    
        """
        tests:
            - test list endpoint (status ok) and returns assigned events       
        mock 3 events.
        must return all events. 
        """
        ## MOCK 
        homepage = PageContainer.objects.create(name='homepage')        
        # create 3 events
        for _ in range(3): 
            Event.objects.create(
            title= f'Event {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
        )        
        # link via many to many with a through model by assigning them directly
        #  via record creation
        for _ in range(1,4): # 1-3
            PageContainedEvent.objects.create(
                container=homepage,
                event= Event.objects.get(pk=_),
                section_order= _,
                )            
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_events'}
            )
        response = self.client.get(url)
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # test number of contained events
        homepage = response.data        
        self.assertEqual(len(homepage['page_contained_events']), 3)

    def test_get_homepage_events_data(self):    
        """
            - test expected event data for homepage
            - mock:
                - homepage
                - 1 event
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')   
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )        
             
        PageContainedEvent.objects.create(
        container=homepage,
        event= event,
        section_order=1,
        )          
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_events.event.image'}
            )
        request = self.request_factory.get(url)  
        response = self.view(request)
        response_contained_event = response.data['page_contained_events'][0]        
        image_url = get_expected_image_url(event.image.image.name, request)
        expected_data = {
            'id': event.id,
            'title': event.title,
                "image": {
                    "id": event.image.id,
                    "image": image_url,
                },
            'description' : event.description,
            'start_date' : to_expected_iso_format(event.start_date),
            'end_date' : to_expected_iso_format(event.end_date),
            'camp' : event.get_camp_display(),
            'created_at': to_expected_iso_format(event.created_at),
            'updated_at': to_expected_iso_format(event.updated_at),
            'status': StatusEnum.PAST.value # based on dates set

            }
        ## TEST
        self.assertDictEqual(expected_data, response_contained_event['event'])


class UpdateHomepageContainerEventsTestCase(APITestCase):
    """
    # test update page_contained_events from homepage    
    - update the event id of a section 

    test cases:
        - test unique all fields
        - test unique event on homepage
        - test unique event section on homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_update_homepage_event_expected(self):
        """
        test:
        expected record is being updated; change event for section. 
        mock:
            - create homepage container
            - create 2 events, assign 1 to homepage via model manager. 
                - the other jumbo will be the one used for the update.
        reqs:
            - no duplicates, no unique constraint violations
            - all fields have entries
        """
        ### MOCK
        # create homepage container
        # create 2 events and reassign only 1. the other shall be for updating
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Event.objects.create(
                title= f'Event {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            )    
        # assign 1 jumbo to homepage
        PageContainedEvent.objects.create(
            container=homepage,
            event=Event.objects.get(pk=1), 
            section_order= 1,
        )     
        update_data = {
                    "container": 1,
                    "event": 2, 
                    "section_order": 1
                }   
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_events": [
                update_data
            ]
        }
        url = reverse('page-container-detail', kwargs={'slug':'homepage'})
        response = self.client.put(
            url,
            data=json.dumps(homepage_with_jumbo_data), #py type to json
            content_type="application/json")
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        ## TEST
        # test if existing record details had been updated
        contained_event = PageContainedEvent.objects.get(pk=1)
        self.assertEqual(contained_event.container.id, update_data['container'])
        self.assertEqual(contained_event.event.id, update_data['event'])
        self.assertEqual(contained_event.section_order, update_data['section_order'])        


    def test_update_homepage_event_create_expected(self):
        """
        create a new contained event via put request. 
        - Current implementation looks at the container and order. If the posted
            - data matches an existing pair (container x order), then it would only
              update that record. 
            - for a new entry to be created, container, order and jumbo must be unique. 
        mock:
            - homepage container
            - 2 events, assign one to homepage
                - other event shall be assigned via put request
        """
        ### MOCK
        # create homepage container
        # create 2 events and reassign only 1. the other shall be assigned
            # by making a put request.
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Event.objects.create(
                title= f'Event {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            )              
        PageContainedEvent.objects.create(
        container=homepage,
        event=Event.objects.first(),
        section_order= 1,
        )     
        ## REQUEST
        new_data =  {
            "container": homepage.id,
            "event": Event.objects.last().id,
            "section_order": 2
        }    

        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_events": [
                new_data
            ]
        }
        url = reverse('page-container-detail', kwargs={'slug':'homepage'})        
        response = self.client.put(
            url,
            data=json.dumps(homepage_with_jumbo_data), #py type to json
            content_type="application/json") 
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(PageContainedEvent.objects.count(), 2)


    def test_error_on_update_homepage_event_exceed_limit(self):
        """
        should not be able to add another when limit is reached.
        mock:
         - homepage container
         - 4 events
         - 3 contained events
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(1,5):   # create 4
            event = Event.objects.create(
                title= f'Event {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            ) 
            # avoid assigning the last (4th) event, since we would want to test
            # that via api
            if not _ == 4: 
                PageContainedEvent.objects.create(
                container=homepage,
                event=event,
                section_order= _,
                )            
        ## REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_events": [
                {
                    "container": 1,
                    "event": 4,
                    "section_order": 4
                }                          
            ]
        }
        url = reverse('page-container-detail', kwargs={'slug':'homepage'})        
        response = self.client.put(
            url,
            data=json.dumps(homepage_with_jumbo_data), #py type to json
            content_type="application/json") 
        error = response.data['detail']
        ## TEST
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code) 
        self.assertEqual(str(error),'Homepage can only contain 3 events at most.') 
        self.assertEqual(error.code, 'invalid')      


    def test_update_homepage_event_with_same_data(self):
        """
        sending exactly the same data would not change the data nor add new
        contained events. 
        mock:
            - homepage container
            - event
            - assign event to homepage container
        test:
            - send put request with the same data
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )               
        contained_event = PageContainedEvent.objects.create(
            container=homepage,
            event=event,
            section_order= 1,
        )     
        ## FOR DATA COMPARISON
        old_data = {
            "container": homepage.id,
            "event": event.id,
            "section_order": 1
        }

        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_events": [
                    old_data                       
            ]
        }
        url = reverse('page-container-detail', kwargs={'slug':'homepage'})        
        response = self.client.put(
            url,
            data=json.dumps(homepage_with_jumbo_data), #py type to json
            content_type="application/json") 
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # test if existing record details had not changed
        self.assertEqual(contained_event.container.id, old_data['container'])
        self.assertEqual(contained_event.event.id, old_data['event'])
        self.assertEqual(contained_event.section_order, old_data['section_order'])


    def test_error_on_update_homepage_event_duplicate_container_jumbo(self):
        """
        updating with the same container and event would create a new record,
        provided the section_order is different. 
        -> should raise an integrity error since events must be unique in homepage.
        mock:
            - homepage container
            - 1 events
            - assign event to homepage container
        test:
            - send put request with the same container and event, but with a
                different section_order.
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )                   
        PageContainedEvent.objects.create(
            container=homepage,
            event=event,
            section_order= 1,
        )
        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_events": [
                {
                    "container": homepage.id,
                    "event": event.id,
                    # attempt to have the same event for slide 1 and 2                    
                    "section_order": 2 
                }                          
            ]
        }
        url = reverse('page-container-detail', kwargs={'slug':'homepage'})
        response = self.client.put(
            url,
            data=json.dumps(homepage_with_jumbo_data), #py type to json
            content_type="application/json") 
        ## TEST
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        error_message = {
        "message": ('UNIQUE constraint failed: '
                    'page_containers_pagecontainedevent.container_id, '
                    'page_containers_pagecontainedevent.event_id')
        }
        self.assertDictEqual(error_message, response.data)


class DeleteHomepageEventTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
    
    def test_delete_contained_event(self):
        """
        delete a contained event using its id.
        mock:
            - homepage container
            - 1 events
            - assign event to homepage container        
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        event = Event.objects.create(
            title= 'Event 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )              
        page_contained_event = PageContainedEvent.objects.create(
            container=homepage,
            event=event,
            section_order= 1,
        )     
        url = reverse('page-contained-event-detail', args=[page_contained_event.id])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

# test delete page_contained_events using another endpoint

        

