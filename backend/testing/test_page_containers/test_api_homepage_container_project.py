import json
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from kalunwa.content.serializers import StatusEnum
from testing.utils import  (
    get_test_image_file,
    get_expected_image_url,
    reverse_with_query_params,
    to_expected_iso_format,    
)
from kalunwa.content.models import(
    Project,
    Image,  
    
)
from kalunwa.page_containers.views import (
    PageContainerDetailView,
)
from kalunwa.page_containers.models import (
    PageContainer,
    PageContainedProject,
)


class GetHomepageContainerProjectsTestCase(APITestCase): 
    """
    # test get page_contained_projects from homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
        cls.view = PageContainerDetailView.as_view()

    # api/page-containers/homepage/
    def test_get_homepage_projects(self):    
        """
        tests:
            - test list endpoint (status ok) and returns assigned projects       
        mock 3 projects.
        must return all projects. 
        """
        ## MOCK 
        homepage = PageContainer.objects.create(name='homepage')        
        # create 3 projects
        for _ in range(3): 
            Project.objects.create(
            title= f'Project {_}', 
            description= f'description {_}',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
        )        
        # link via many to many with a through model by assigning them directly
        #  via record creation
        for _ in range(1,4): # 1-3
            PageContainedProject.objects.create(
                container=homepage,
                project= Project.objects.get(pk=_),
                section_order= _,
                )            
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_projects'}
            )
        response = self.client.get(url)
        ## TEST
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # test number of contained projects
        homepage = response.data        
        self.assertEqual(len(homepage['page_contained_projects']), 3)

    def test_get_homepage_projects_data(self):    
        """
            - test expected project data for homepage
            - mock:
                - homepage
                - 1 project
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')   
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date= timezone.now(),
            end_date= timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )        
             
        PageContainedProject.objects.create(
        container=homepage,
        project= project,
        section_order=1,
        )          
        ## REQUEST
        url = reverse_with_query_params(
            viewname='page-container-detail',
            kwargs={'slug':'homepage'}, 
            query_kwargs={'expand':'page_contained_projects.project.image'}
            )
        request = self.request_factory.get(url)  
        response = self.view(request)
        response_contained_project = response.data['page_contained_projects'][0]        
        image_url = get_expected_image_url(project.image.image.name, request)
        expected_data = {
            'id': project.id,
            'title': project.title,
                "image": {
                    "id": project.image.id,
                    "image": image_url,
                },
            'description' : project.description,
            'start_date' : to_expected_iso_format(project.start_date),
            'end_date' : to_expected_iso_format(project.end_date),
            'camp' : project.get_camp_display(),
            'created_at': to_expected_iso_format(project.created_at),
            'updated_at': to_expected_iso_format(project.updated_at),
            'status': StatusEnum.PAST.value # based on dates set

            }
        ## TEST
        self.assertDictEqual(expected_data, response_contained_project['project'])


class UpdateHomepageContainerProjectsTestCase(APITestCase):
    """
    # test update page_contained_projects from homepage    
    - update the project id of a section 

    test cases:
        - test unique all fields
        - test unique project on homepage
        - test unique project section on homepage
    """
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()

    def test_update_homepage_project_expected(self):
        """
        test:
        expected record is being updated; change project for section. 
        mock:
            - create homepage container
            - create 2 projects, assign 1 to homepage via model manager. 
                - the other jumbo will be the one used for the update.
        reqs:
            - no duplicates, no unique constraint violations
            - all fields have entries
        """
        ### MOCK
        # create homepage container
        # create 2 projects and reassign only 1. the other shall be for updating
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Project.objects.create(
                title= f'Project {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            )    
        # assign 1 jumbo to homepage
        PageContainedProject.objects.create(
            container=homepage,
            project=Project.objects.get(pk=1), 
            section_order= 1,
        )     
        update_data = {
                    "container": 1,
                    "project": 2, 
                    "section_order": 1
                }   
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_projects": [
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
        contained_project = PageContainedProject.objects.get(pk=1)
        self.assertEqual(contained_project.container.id, update_data['container'])
        self.assertEqual(contained_project.project.id, update_data['project'])
        self.assertEqual(contained_project.section_order, update_data['section_order'])        


    def test_update_homepage_project_create_expected(self):
        """
        create a new contained project via put request. 
        - Current implementation looks at the container and order. If the posted
            - data matches an existing pair (container x order), then it would only
              update that record. 
            - for a new entry to be created, container, order and jumbo must be unique. 
        mock:
            - homepage container
            - 2 projects, assign one to homepage
                - other project shall be assigned via put request
        """
        ### MOCK
        # create homepage container
        # create 2 projects and reassign only 1. the other shall be assigned
            # by making a put request.
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(2):   
            Project.objects.create(
                title= f'Project {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            )              
        PageContainedProject.objects.create(
        container=homepage,
        project=Project.objects.first(),
        section_order= 1,
        )     
        ## REQUEST
        new_data =  {
            "container": homepage.id,
            "project": Project.objects.last().id,
            "section_order": 2
        }    

        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_projects": [
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
        self.assertEqual(PageContainedProject.objects.count(), 2)


    def test_error_on_update_homepage_project_exceed_limit(self):
        """
        should not be able to add another when limit is reached.
        mock:
         - homepage container
         - 4 projects
         - 3 contained projects
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        for _ in range(1,5):   # create 4
            project = Project.objects.create(
                title= f'Project {_}', 
                description= f'description {_}',
                start_date=timezone.now(),
                end_date=timezone.now(),
                image = Image.objects.create(name=f'image_{_}', image=self.image_file), 
            ) 
            # avoid assigning the last (4th) project, since we would want to test
            # that via api
            if not _ == 4: 
                PageContainedProject.objects.create(
                container=homepage,
                project=project,
                section_order= _,
                )            
        ## REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_projects": [
                {
                    "container": 1,
                    "project": 4,
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
        self.assertEqual(str(error),'Homepage can only contain 3 projects at most.') 
        self.assertEqual(error.code, 'invalid')      


    def test_update_homepage_project_with_same_data(self):
        """
        sending exactly the same data would not change the data nor add new
        contained projects. 
        mock:
            - homepage container
            - project
            - assign project to homepage container
        test:
            - send put request with the same data
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )               
        contained_project = PageContainedProject.objects.create(
            container=homepage,
            project=project,
            section_order= 1,
        )     
        ## FOR DATA COMPARISON
        old_data = {
            "container": homepage.id,
            "project": project.id,
            "section_order": 1
        }

        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_projects": [
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
        self.assertEqual(contained_project.container.id, old_data['container'])
        self.assertEqual(contained_project.project.id, old_data['project'])
        self.assertEqual(contained_project.section_order, old_data['section_order'])


    def test_error_on_update_homepage_project_duplicate_container_jumbo(self):
        """
        updating with the same container and project would create a new record,
        provided the section_order is different. 
        -> should raise an integrity error since projects must be unique in homepage.
        mock:
            - homepage container
            - 1 projects
            - assign project to homepage container
        test:
            - send put request with the same container and project, but with a
                different section_order.
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )                   
        PageContainedProject.objects.create(
            container=homepage,
            project=project,
            section_order= 1,
        )
        ## PUT REQUEST
        homepage_with_jumbo_data = {
            "name": "homepage",
            "page_contained_projects": [
                {
                    "container": homepage.id,
                    "project": project.id,
                    # attempt to have the same project for slide 1 and 2                    
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
                    'page_containers_pagecontainedproject.container_id, '
                    'page_containers_pagecontainedproject.project_id')
        }
        self.assertDictEqual(error_message, response.data)


class DeleteHomepageProjectTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.image_file = get_test_image_file()
        cls.request_factory = APIRequestFactory()
    
    def test_delete_contained_project(self):
        """
        delete a contained project using its id.
        mock:
            - homepage container
            - 1 projects
            - assign project to homepage container        
        """
        ## MOCK
        homepage = PageContainer.objects.create(name='homepage')
        project = Project.objects.create(
            title= 'Project 1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            image = Image.objects.create(name='image_1', image=self.image_file),
        )              
        page_contained_project = PageContainedProject.objects.create(
            container=homepage,
            project=project,
            section_order= 1,
        )     
        url = reverse('page-contained-project-detail', args=[page_contained_project.id])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

# test delete page_contained_projects using another endpoint

        

