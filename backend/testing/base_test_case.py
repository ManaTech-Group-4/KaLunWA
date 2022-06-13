from django.urls import reverse
from rest_framework.test import APITestCase
from kalunwa.users.models import (
    User,
)

class BaseUserTestCase(APITestCase):
    user_credentials = {
        'email':'test@test.com',
        'password':'test123456'        
    }
    admin_credentials = {
        'email':'admin@test.com',
        'password':'admin123456'
    }    

    def create_user(self):
        user = User.objects.create_user(
            email=self.user_credentials['email'],
            password=self.user_credentials['password']
        )
        return user

    def create_superuser(self):
        User.objects.create_superuser(
            email=self.admin_credentials['email'],
            password=self.admin_credentials['password']
        )

    def get_superuser_tokens(self):
        self.create_superuser()
        url = reverse('token-obtain-pair')
        response = self.client.post(url, self.admin_credentials)   
        return response.data  

    def get_user_tokens(self):
        self.create_user()
        url = reverse('token-obtain-pair')
        response = self.client.post(url, self.user_credentials)   
        return response.data     

class BaseWithClientCredentialsTestCase(BaseUserTestCase):
    def load_user_client_credentials(self, token=None):
        if not token:
            tokens = self.get_user_tokens()
            token = tokens['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def load_superuser_client_credentials(self, token=None):
        if not token:
            tokens = self.get_superuser_tokens()
            token = tokens['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)       