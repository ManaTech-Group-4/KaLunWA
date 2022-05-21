import json
from rest_framework.test import (
    APITestCase, 
    APIRequestFactory
)
from django.test.client import (
    MULTIPART_CONTENT,
    encode_multipart, 
    BOUNDARY # separates parameters of form using a boundary 
)
from django.core.files.base import ContentFile  
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
    @classmethod
    def setUpTestData(cls) -> None:
        cls.request_factory = APIRequestFactory()

    def setUp(self) -> None: 
        # using set up here to reset image file, as we would have to seek
            # for the file to not be empty (upload raises invalid due to empty file
            # if this is not done)
        self.image_file = get_test_image_file()

    def test_valid_upload(self):
        # set the file's current position, put it on stream via seek
        # if not added, will be considered as empty file and view will raise an error         
        self.image_file.seek(0) 
        url = reverse("image-list")
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(image=self.image_file, name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
           # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )        
        self.assertEqual(201, response.status_code)
    
    def test_upload_response_data(self):
        self.image_file.seek(0) 
        url = reverse("image-list")
        response = self.client.post(
            path=url,
            data=encode_multipart(data = dict(image=self.image_file, name="test"), boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
           # HTTP_AUTHORIZATION=f"Token {self.token.key}" # -> to add when authentication is implemented
        )        

        response_image_data = json.loads(response.content) # json to py data types
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



    
