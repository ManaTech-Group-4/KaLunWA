
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from kalunwa.content.models import CampEnum, Image, Jumbotron, Tag, Event
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from django.utils import timezone

class HomapageActionsTestCase(APITestCase):
    """
    Test homepage endpoints
    """
    @classmethod
    def setUpTestData(cls):
        """
        set ups data that will not be changed in the class. 
        vs. 
        setUp, expects changes & refreshes for every test method.
        """
        # create non-storable file for image upload 
            # 37-byte GIF 1 white pixel
            #  inorder not to create big files in the system

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
            # currently mock implementation
        image_upload = SimpleUploadedFile('small.gif', small_gif,
         content_type='image/gif')

        image = Image.objects.create(
            title='eating_me',
            image=image_upload,
        )

        # create tags for image
        for _ in range(3): 
            Tag.objects.create(
            name=f'tag_{_}'
            )

        tags = Tag.objects.all()
        image.tags.set(tags)

        # create Jumbotrons
        for _ in range(3): 
            Jumbotron.objects.create(
            header_title= 'J1', 
            short_description= 'short description 1',
            image = image
            )

        # create Events
            Event.objects.create(
            title= 'E1', 
            description= 'description 1',
            start_date=timezone.now(),
            end_date=timezone.now(),
            camp=CampEnum.GENERAL,
            image = image,
            is_featured=True,
            )            

        ## class attribute    
        cls.jumbotrons = Jumbotron.objects.all()
        cls.events = Event.objects.all()


    def test_get_homepage_jumbotrons(self):
        """
        Tests list endpoints for homepage jumbotrons.

        - reverses a url name to get its path, asusing full paths may not work
         during deployment given it is server dependent.

        --> /api/homepage/jumbotrons/ 
        instead of:
        --> http://127.0.0.1:8000/api/homepage/jumbotrons/

        - response.data returns arrays of ordered dicts
        - self.jumbotrons returns querysets
        """
        # reverse returns (/api/homepage/jumbotrons/)
        response = self.client.get(reverse("homepage-jumbotrons"))
        
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        # checks if all generated jumbotrons were fetched
        self.assertEquals(len(self.jumbotrons), len(response.data))


    def test_get_homepage_events(self):
        """
        Note that this view only retrieves featured events, with a limit of 3.
        Requirement for fetched objects should be is_featured.
        """
        response = self.client.get(reverse("homepage-events"))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.events), len(response.data))
        # print(self.__class__.jumbotrons[0].image.image)

        # sample response.data 
        # [OrderedDict([('id', 1), ('title', 'E1'), ('image', 'http://testserver/media/images/content/small_s3QdcNl.gif')])]    
        #response.data[0]['image'] -> 'http://testserver/media/images/content/small_s3QdcNl.gif')

    # def test_get_homepage_projects(self):
    #     pass

    # def test_get_homepage_news(self):
    #     pass
        

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
        image = Image.objects.get(pk=obj.image.pk)
        """
        image = Image.objects.get(pk=self.__class__.jumbotron.image.id)
        self.assertEqual(self.__class__.image.id,image.id)


    
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