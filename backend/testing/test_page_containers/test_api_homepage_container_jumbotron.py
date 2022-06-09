import json
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from testing.utils import  (
    get_test_image_file,
    get_expected_image_url,
    reverse_with_query_params,
    to_expected_iso_format,    
)
from kalunwa.content.models import(
    Image, 
    Jumbotron,  
)
from kalunwa.page_containers.views import (
    PageContainerListView,
    PageContainerDetailView,
)
from kalunwa.page_containers.models import (
    PageContainer,
    PageContainedJumbotron,
)

class GetHomepageContainerJumbotronsTestCase(APITestCase): 
    """
    # test get page_contained_jumbotrons from homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.view = PageContainerDetailView.as_view()

    # api/page-containers/homepage/
    def test_get_homepage_jumbotrons(self):    
        """
        tests:
            - test list endpoint (status ok) and returns assigned jumbotrons       
        mock 5 jumbotrons.
        must return all jumbotrons. 
        """
        ## MOCK 
        homepage = PageContainer.objects.create(name='homepage')        
        # create 5 jumbotrons
        for _ in range(5): 
            Jumbotron.objects.create(
                header_title= f'Jumbotron {_}', 
                subtitle= f'short description {_}',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file),               
            )      
        # link via many to many with a through model by assigning them directly
        #  via record creation
        for _ in range(1,6): # 1- 5
            PageContainedJumbotron.objects.create(
                container=homepage,
                jumbotron= Jumbotron.objects.get(pk=_),
                section_order= _,
                )            
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_jumbotrons'}
            )
        response = self.client.get(url)
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # test number of contained jumbotrons
        homepage = response.data        
        self.assertEqual(len(homepage['page_contained_jumbotrons']), 5)

    def test_get_homepage_jumbotrons_data(self):    
        """
            - test expected jumbotron data for homepage
            - mock:
                - homepage
                - 1 jumbotron
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')   
        jumbotron = Jumbotron.objects.create(
            header_title= f'Jumbotron {1}', 
            subtitle= f'short description {1}',
            image = Image.objects.create(name=f'image_{1}', image=self.image_file),               
        )               
        PageContainedJumbotron.objects.create(
        container=homepage,
        jumbotron= jumbotron,
        section_order= 1,
        )          
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_jumbotrons.jumbotron.image'}
            )        
        request = self.request_factory.get(url)  
        response = self.view(request)
        response_contained_jumbotron = response.data['page_contained_jumbotrons'][0]        
        image_url = get_expected_image_url(jumbotron.image.image.name, request)
        expected_data = {
                "id": jumbotron.id,
                "header_title": jumbotron.header_title,
                "subtitle": jumbotron.subtitle,
                "image": {
                    "id": jumbotron.image.id,
                    "image": image_url,
                },
            'created_at': to_expected_iso_format(jumbotron.created_at),
            'updated_at': to_expected_iso_format(jumbotron.updated_at),
            }
        ## TEST
        self.assertDictEqual(expected_data, response_contained_jumbotron['jumbotron'])


class UpdateHomepageContainerJumbotronsTestCase(APITestCase):
    """
    # test update page_contained_jumbotrons from homepage    
    - update the jumbotron id of a section 

    test cases:
        - test unique all fields
        - test unique jumbotron on homepage
        - test unique jumbotron section on homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_update_homepage_jumbotron_expected(self):
        """
        test:
        expected record is being updated; change jumbotron for section. 
        mock:
            - create homepage container
            - create 2 jumbotrons, assign 1 to homepage via model manager. 
                - the other jumbo will be the one used for the update.
        reqs:
            - no duplicates, no unique constraint violations
            - all fields have entries
        """
        ### MOCK
        # create homepage container
        # create 2 jumbotrons and reassign only 1. the other shall be for updating
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Jumbotron.objects.create(
                header_title= f'Jumbotron {_}', 
                subtitle= f'short description {_}',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file),               
            )        
        # assign 1 jumbo to homepage
        PageContainedJumbotron.objects.create(
            container=homepage,
            jumbotron=Jumbotron.objects.get(pk=1), 
            section_order= 1,
        )     
        update_data = {
                    "container": 1,
                    "jumbotron": 2, 
                    "section_order": 1
                }   
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_jumbotrons": [
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
        contained_jumbotron = PageContainedJumbotron.objects.get(pk=1)
        self.assertEqual(contained_jumbotron.container.id, update_data['container'])
        self.assertEqual(contained_jumbotron.jumbotron.id, update_data['jumbotron'])
        self.assertEqual(contained_jumbotron.section_order, update_data['section_order'])        


    def test_update_homepage_jumbotron_create_expected(self):
        """
        create a new contained jumbotron via put request. 
        - Current implementation looks at the container and order. If the posted
            - data matches an existing pair (container x order), then it would only
              update that record. 
            - for a new entry to be created, container, order and jumbo must be unique. 
        mock:
            - homepage container
            - 2 jumbotrons, assign one to homepage
                - other jumbotron shall be assigned via put request
        """
        ### MOCK
        # create homepage container
        # create 2 jumbotrons and reassign only 1. the other shall be assigned
            # by making a put request.
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Jumbotron.objects.create(
                header_title= f'Jumbotron {_}', 
                subtitle= f'short description {_}',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file),               
            )               
        PageContainedJumbotron.objects.create(
        container=homepage,
        jumbotron=Jumbotron.objects.first(),
        section_order= 1,
        )     
        ## REQUEST
        new_data =  {
            "container": homepage.id,
            "jumbotron": Jumbotron.objects.last().id,
            "section_order": 2
        }    

        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_jumbotrons": [
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
        self.assertEqual(PageContainedJumbotron.objects.count(), 2)


    def test_error_on_update_homepage_jumbotron_exceed_limit(self):
        """
        should not be able to add another when limit is reached.
        mock:
         - homepage container
         - 6 jumbotrons
         - 5 contained jumbotrons
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(1,7):   
            jumbotron = Jumbotron.objects.create(
                header_title= f'Jumbotron {_}', 
                subtitle= f'short description {_}',
                image = Image.objects.create(name=f'image_{_}', image=self.image_file),               
            ) 
            if not _ == 6: # avoid assigning the last jumbotron
                PageContainedJumbotron.objects.create(
                container=homepage,
                jumbotron=jumbotron,
                section_order= _,
                )            
        ## REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_jumbotrons": [
                {
                    "container": 1,
                    "jumbotron": 6,
                    "section_order": 6
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
        self.assertEqual(str(error),'Homepage can only contain 5 jumbotrons at most.') 
        self.assertEqual(error.code, 'invalid')      


    def test_update_homepage_jumbotron_with_same_data(self):
        """
        sending exactly the same data would not change the data nor add new
        contained jumbotrons. 
        mock:
            - homepage container
            - jumbotron
            - assign jumbotron to homepage container
        test:
            - send put request with the same data
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        jumbotron = Jumbotron.objects.create(
            header_title= f'Jumbotron {1}', 
            subtitle= f'short description {1}',
            image = Image.objects.create(name=f'image_{1}', image=self.image_file),               
        )               
        contained_jumbotron = PageContainedJumbotron.objects.create(
            container=homepage,
            jumbotron=jumbotron,
            section_order= 1,
        )     
        ## FOR DATA COMPARISON
        old_data = {
            "container": homepage.id,
            "jumbotron": jumbotron.id,
            "section_order": 1
        }

        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_jumbotrons": [
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
        self.assertEqual(contained_jumbotron.container.id, old_data['container'])
        self.assertEqual(contained_jumbotron.jumbotron.id, old_data['jumbotron'])
        self.assertEqual(contained_jumbotron.section_order, old_data['section_order'])


    def test_error_on_update_homepage_jumbotron_duplicate_container_jumbo(self):
        """
        updating with the same container and jumbotron would create a new record,
        provided the section_order is different. 
        -> should raise an integrity error since jumbotrons must be unique in homepage.
        mock:
            - homepage container
            - 1 jumbotrons
            - assign jumbotron to homepage container
        test:
            - send put request with the same container and jumbotron, but with a
                different section_order.
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        jumbotron = Jumbotron.objects.create(
            header_title= f'Jumbotron {1}', 
            subtitle= f'short description {1}',
            image = Image.objects.create(name=f'image_{1}', image=self.image_file),               
        )               
        PageContainedJumbotron.objects.create(
            container=homepage,
            jumbotron=jumbotron,
            section_order= 1,
        )
        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_jumbotrons": [
                {
                    "container": homepage.id,
                    "jumbotron": jumbotron.id,
                    # attempt to have the same jumbotron for slide 1 and 2                    
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
                    'page_containers_pagecontainedjumbotron.container_id, '
                    'page_containers_pagecontainedjumbotron.jumbotron_id')
        }
        self.assertDictEqual(error_message, response.data)


class DeleteHomepageJumbotronTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
    
    def test_delete_contained_jumbotron(self):
        """
        delete a contained jumbotron using its id.
        mock:
            - homepage container
            - 1 jumbotrons
            - assign jumbotron to homepage container        
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        jumbotron = Jumbotron.objects.create(
            header_title= f'Jumbotron {1}', 
            subtitle= f'short description {1}',
            image = Image.objects.create(name=f'image_{1}', image=self.image_file),               
        )               
        page_contained_jumbotron = PageContainedJumbotron.objects.create(
            container=homepage,
            jumbotron=jumbotron,
            section_order= 1,
        )     
        url = reverse('page-contained-jumbotron-detail', args=[page_contained_jumbotron.id])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

# test delete page_contained_jumbotrons using another endpoint

        

