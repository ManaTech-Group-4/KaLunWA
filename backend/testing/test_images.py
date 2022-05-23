import json
from rest_framework import status
from rest_framework.test import (
    APITestCase, 
    APIRequestFactory
)
from django.test.client import (
    MULTIPART_CONTENT,
    encode_multipart, 
    BOUNDARY # separates parameters of form using a boundary 
)
from django.urls import reverse
from testing.utils import (
    get_expected_image_url, 
    get_test_image_file, 
    to_expected_iso_format
) 
from kalunwa.content.models import (
    Image
)

class ImageUploadTestCase(APITestCase):     
    """
    Post valid image upload. Uses multipart/form-data.
    - status create OK, 201 
    """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.request_factory = APIRequestFactory()

    def setUp(self) -> None: 
        # using set up here to reset image file, as we would have to seek
            # for the file to not be empty (upload raises invalid due to empty file
            # if this is not done)
        self.image_file = get_test_image_file()

    def test_valid_upload(self):
        """
        has expected fields filled up. should create record as by returning 
        status code 201
        """
        # set the file's current position, put it on stream via seek
        # if not added, will be considered as empty file and view will raise an error         
        self.image_file.seek(0) 
        url = reverse("image-list")
        # dict would hold the key-value parameters from a form
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(name="test", image=self.image_file), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
           # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    
    def test_upload_response_data(self):
        """
        test data returned after a successful upload. It should return all fields. 
        """
        self.image_file.seek(0) 
        url = reverse("image-list")
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(image=self.image_file, name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
           # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )        
        response_image_data = json.loads(response.content) # json to py data types
        # create request to generate image url 
        request = self.request_factory.post(
            path=url,
            data=encode_multipart(
                data = dict(image=self.image_file, name="test"), 
                boundary=BOUNDARY), 
                content_type=MULTIPART_CONTENT,            
        )
        expected_image = Image.objects.first()
        expected_image_data = {
            'id': expected_image.id, 
            'name': expected_image.name, 
            'image': get_expected_image_url(expected_image.image.name, request),
            'tags': [], 
            'created_at': to_expected_iso_format(expected_image.created_at),
            'updated_at': to_expected_iso_format(expected_image.updated_at)
        }
        self.assertDictEqual(expected_image_data, response_image_data)

    def test_empty_image_file_upload(self):
        """
        test upload empty image file. should return status code 404. 
        file is empty here because it had not been used with seek, 
        which should set the file to the stream
        """
        url = reverse("image-list")
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(image=self.image_file, name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )  
        error = response.data['image'][0] # error_detail object
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error.title(), 'The Submitted File Is Empty.')
        self.assertEqual(error.code, 'empty')

    def test_invalid_image_upload(self):
        """
        test invalid image upload via string. should return status code 404. 
        """
        url = reverse("image-list")
        image = 'to test string upload'
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(image=image, name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )  
        error = response.data['image'][0]
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error.title(), 'The Submitted Data Was Not A File. Check The Encoding Type On The Form.')
        self.assertEqual(error.code, 'invalid')


    def test_no_image_file_upload(self):
        """
        test upload no file. should return status code 404 since image file
        is required.
        """
        url = reverse("image-list")
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
        # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )  
        error = response.data['image'][0]
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error.title(), 'No File Was Submitted.')
        self.assertEqual(error.code, 'required')