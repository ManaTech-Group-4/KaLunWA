
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from kalunwa.content.models import CampEnum, Image, Jumbotron, News, Project, Tag, Event
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from django.utils import timezone

# class HomapageActionsTestCase(APITestCase):
#     """
#     Test homepage endpoints
#     """
#     @classmethod
#     def setUpTestData(cls):
#         """
#         set ups data that will not be changed in the class. 
#         vs. 
#         setUp, expects changes & refreshes for every test method.
#         """
#         # create non-storable file for image upload 
#             # 37-byte GIF 1 white pixel
#             #  inorder not to create big files in the system

#         small_gif = (
#             b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
#             b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
#             b'\x02\x4c\x01\x00\x3b'
#         )
#         # currently mock implementation
#         image_upload = SimpleUploadedFile('small.gif', small_gif,
#          content_type='image/gif')

#         # create tags for image
#         for _ in range(3): 
#             Image.objects.create(
#                 pk=_,
#                 title=f'image_{_}',
#                 image=image_upload,
#             )            

#         # create content
#         for _ in range(3): 
#         # create Jumbotrons
#             Jumbotron.objects.create(
#             header_title= f'Jumbotron {_}', 
#             short_description= f'short description {_}',
#             image = Image.objects.get(pk=_)
#             )

#         # create Events (featured) 
#             Event.objects.create(
#             title= f'Event {_}', 
#             description= f'description {_}',
#             start_date=timezone.now(),
#             end_date=timezone.now(),
#             camp=CampEnum.GENERAL,
#             image = Image.objects.get(pk=_),
#             is_featured=True,
#             )            

#         # create Projects (featured) 
#             Project.objects.create(
#             title= f'Project {_}', 
#             description= 'description {_}',
#             start_date=timezone.now(),
#             end_date=timezone.now(),
#             camp=CampEnum.GENERAL,
#             image = Image.objects.get(pk=_),
#             is_featured=True,
#             )            

#             News.objects.create(
#                 title = f'News {_}',
#                 description= 'description {_}',
#                 image = Image.objects.get(pk=_),
#             )

#         ## class attribute    
#         cls.jumbotrons = Jumbotron.objects.all()
#         cls.events = Event.objects.all()
#         cls.projects = Project.objects.all()
#         cls.news = Project.objects.all()


#     def test_get_homepage_jumbotrons(self):
#         """
#         Tests list endpoints for homepage jumbotrons.

#         - reverses a url name to get its path, as using full paths may not work
#          during deployment given it is server dependent.

#         --> /api/homepage/jumbotrons/ 
#         instead of:
#         --> http://127.0.0.1:8000/api/homepage/jumbotrons/

#         - response.data returns arrays of ordered dicts
#         - self.jumbotrons returns querysets
#         """
#         # reverse returns (/api/homepage/jumbotrons/)
#         response = self.client.get(reverse("homepage-jumbotrons"))
        
#         self.assertEquals(status.HTTP_200_OK, response.status_code)

#         # checks if all generated jumbotrons were fetched
#         self.assertEquals(len(self.jumbotrons), len(response.data))


#     def test_get_homepage_events(self):
#         """
#         Note that this view only retrieves featured events, with a limit of 3.
#         Requirement for fetched objects should be is_featured.
#         """
#         response = self.client.get(reverse("homepage-events"))
#         self.assertEquals(status.HTTP_200_OK, response.status_code)
#         self.assertEquals(len(self.events), len(response.data))
#         # print(self.__class__.jumbotrons[0].image.image) -> access class attribute

#         # sample response.data 
#         # [OrderedDict([('id', 1), ('title', 'E1'), ('image', 'http://testserver/media/images/content/small_s3QdcNl.gif')])]    
#         #response.data[0]['image'] -> 'http://testserver/media/images/content/small_s3QdcNl.gif')

#     def test_get_homepage_projects(self):
#         response = self.client.get(reverse("homepage-projects"))
#         self.assertEquals(status.HTTP_200_OK, response.status_code)
#         self.assertEquals(len(self.projects), len(response.data))

#     def test_get_homepage_news(self):
#         response = self.client.get(reverse("homepage-news"))
#         self.assertEquals(status.HTTP_200_OK, response.status_code)
#         self.assertEquals(len(self.news), len(response.data))
        

    # def test_retrieve_image_from_obj_field(self):
    #    pass

    
# ---------------------------------------------------------------------------        
class JumbotronImageTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
            # currently mock implementation
        image_upload = SimpleUploadedFile('small.gif', small_gif,
        content_type='image/gif')

        cls.image = Image.objects.create(
            title='eating_me',
            image=image_upload,
        )

        cls.jumbotron = Jumbotron.objects.create(
            id=1, 
            header_title= 'J1', 
            short_description= 'short description 1',
            image = cls.image
        )

    def test_get_object_image_pk(self):
        """
        test for:
        image = Image.objects.get(pk=obj.image.pk)
        """
        image = Image.objects.get(pk=self.__class__.jumbotron.image.id)
        self.assertEqual(self.__class__.image, image)


    
    # def test_get_serialized_image_url_with_context(self):
    #                 pass



# ---------------------------------------------------------------------------        
        #return array of jumbotrons from endpoint & compare data
        # id
        # title
        # short_description
        # http://127.0.0.1:8000/media/images/content/small.gif
# ---------------------------------------------------------
# test to get absolute url of image
# ---------------------------------------------------------



# python manage.py test kalunwa.content.tests.test_apis
# coverage run manage.py test kalunwa.content.tests.test_apis