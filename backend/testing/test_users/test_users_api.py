# test user registration (creation)


# test user login
"""
mock:
 - create user
test:
 - return access and refresh tokens 
 - can we take a look at these tokens? or maybe their payload lng. 
"""
## MOCK

# test user verify
# test refresh token
# test user delete 
# test user logout
from django.urls import reverse
from rest_framework import status
from kalunwa.users.models import (
    User,
)
from testing.base_test_case import BaseUserTestCase, BaseWithClientCredentialsTestCase

class UserLoginTestCase(BaseUserTestCase):

    def test_user_login_via_token(self):
        ## MOCK
        self.create_user()
        ## SET-UP
        url = reverse('token-obtain-pair')
        response = self.client.post(url, self.user_credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for key in response.data.keys():
            self.assertIn(key, ['access', 'refresh'])

    def test_invalid_user_login_via_token(self):
        """
        Tests non-existent user attempts.
        -- No active account found with the given credentials.
        """
        ## SET-UP
        user_credentials = {
            "email" : "test2@test.com",
            "password" : "test123456"
        }
        url = reverse('token-obtain-pair')
        response = self.client.post(url, user_credentials) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)           


class UserBlackListLogoutTestCase(BaseWithClientCredentialsTestCase):
    """
    Blacklisting a token disables the blacklisted refresh token to generate 
    another access token. 
    """

    def test_blacklist_user_via_refresh_token(self):
        tokens = self.get_user_tokens()
        url = reverse('token-blacklist')
        response = self.client.post(url, {
            "refresh" : tokens['refresh']
        })        
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_blacklist_user_via_access_token(self):
        """
        blacklist endpoint does not acknowledge access tokens.
        """
        tokens = self.get_user_tokens()
        url = reverse('token-blacklist')
        response = self.client.post(url, {
            "refresh" : tokens['access']
        })        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blacklist_user_via_invalid_token(self):
        url = reverse('token-blacklist')
        response = self.client.post(url, {
            "refresh" : 'invalid'
        })        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blacklist_token_then_attempt_refresh(self):
        ## BLACKLIST
        tokens = self.get_user_tokens()
        url = reverse('token-blacklist')
        refresh_token = {
            "refresh" : tokens['refresh']
        }
        response = self.client.post(url, refresh_token)        
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        ## ATTEMPT REFRESH
        url = reverse('token-refresh')
        response = self.client.post(url, refresh_token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)        


class RefreshTokenTestCase(BaseUserTestCase):
    """
    Submit refresh token to get an access token.
    """
    def test_valid_refresh_token(self):
        tokens = self.get_user_tokens()
        url = reverse('token-refresh')
        refresh = {
            "refresh" : tokens['refresh']
        }
        response = self.client.post(url, refresh)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data.keys())
        self.assertNotEqual(response.data['access'], tokens['access'])

    def test_invalid_refresh_token(self):
        url = reverse('token-refresh')
        invalid_refresh = {
            "refresh": "test"
        }
        response = self.client.post(url, invalid_refresh)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class VerifyTokenTestCase(BaseUserTestCase):
    """
    lacks capability to expire token, so expired tokens are not tested against
    these.
    --> may do it via blacklist
    """
    def test_valid_access_and_refresh_token(self):
        """
        Tests valid refresh and tokens against the verify endpoint. 
        # Verify endpoint checks if the token had not expired yet, but does 
        not check if it is blacklisted or not. 
        e.g. blacklisted refresh is still regarded as verified.
        """
        tokens = self.get_user_tokens()
        url = reverse('token-verify') 

        for token in tokens.values(): # access and refresh
            token = {
                "token" : token
            }
            response = self.client.post(url, token)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_token(self):
        url = reverse('token-verify')  
        token = {
            "token" : "test"
        }         
        response = self.client.post(url, token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_verify_on_blacklisted_refresh_token(self):
        """
        When blacklisting a refresh token, it does not force expire it. So it 
        would still be considered as a valid token in the verifier. However
        it cannot generate new access tokens anymore.
        """
        tokens = self.get_user_tokens()
        url = reverse('token-blacklist')
        token = {
            "refresh" : tokens['refresh']
        }
        # blacklist before verifying
        response = self.client.post(url, token)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        token = {
            "token" : tokens['refresh']
        }        
        url = reverse('token-verify')
        response = self.client.post(url, token)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_verify_access_token_after_its_refresh_token_is_blacklisted(self):
        """
        Blacklisting refresh tokens means that one cannot refresh their access tokens. 
        But that does not force expire an access token, so it would still be 
        valid.
        """
        tokens = self.get_user_tokens()
        url = reverse('token-blacklist')
        refresh_token = {
            "refresh" : tokens['refresh']
        }
        response = self.client.post(url, refresh_token)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        # prep for verifying
        access_token = {
            "token" : tokens['access']
        }        
        url = reverse('token-verify')
        response = self.client.post(url, access_token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)



class UserRegistrationTestCase(BaseWithClientCredentialsTestCase):
    """
    Only Superusers can create/register users.
    """

    def test_user_registration_with_superuser_and_valid_access_token(self):
        self.load_superuser_client_credentials()
        url = reverse('user-register')
        response = self.client.post(url, self.user_credentials)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_user_registration_with_superuser_and_with_refresh_token(self):
        """
        Since refresh tokens do not serve authentication purposes, this raises 
        a 401 unauthorized error code.
        """
        tokens = self.get_superuser_tokens()
        self.load_superuser_client_credentials(token=tokens['refresh'])
        url = reverse('user-register')
        response = self.client.post(url, self.user_credentials)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_registration_with_invalid_access_token(self):
        url = reverse('user-register')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'invalid')
        response = self.client.post(url, self.user_credentials)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_registration_normal_user(self):
        tokens = self.get_user_tokens()
        self.load_user_client_credentials(token=tokens['access'])
        url = reverse('user-register')
        response = self.client.post(url, self.user_credentials)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 


class UserViewDetailTestCase(BaseWithClientCredentialsTestCase):
    """
    Only Authenticated clients are allowed 
    """
    def test_unauthenticated_user_view_detail(self):
        # unauthorized
        self.create_user() # to have something to retrieve
        url = reverse('user-detail', kwargs={"pk":"1"})
        response = self.client.get(url)    
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)                  

    def test_authenticated_user_view_detail(self):
        self.load_user_client_credentials()
        url = reverse('user-detail', kwargs={"pk":"1"})
        response = self.client.get(url)    
        self.assertEqual(response.status_code, status.HTTP_200_OK)           

    def test_superuser_view_detail(self):
        self.load_superuser_client_credentials()
        url = reverse('user-detail', kwargs={"pk":"1"})
        response = self.client.get(url)     
        self.assertEqual(response.status_code, status.HTTP_200_OK)     


class UserViewListTestCase(BaseWithClientCredentialsTestCase):
    """
    Only Authenticated clients are allowed 
    """
    def test_unauthenticated_user_view_detail(self):
        # unauthorized
        self.create_user() # to have something to retrieve
        url = reverse('user-list')
        response = self.client.get(url)    
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)                  

    def test_authenticated_user_view_detail(self):
        self.load_user_client_credentials()
        url = reverse('user-list')
        response = self.client.get(url)    
        self.assertEqual(response.status_code, status.HTTP_200_OK)           

    def test_superuser_view_detail(self):
        self.load_superuser_client_credentials()
        url = reverse('user-list')
        response = self.client.get(url)     
        self.assertEqual(response.status_code, status.HTTP_200_OK)  


class UserChangePasswordTestCase(BaseWithClientCredentialsTestCase):

    def user_changes_password_with_correct_old_password(self):
        tokens = self.get_user_tokens()
        self.load_user_client_credentials(tokens["access"]) 
        url = reverse('user-change-password')
        new_password = 12345678
        user = User.objects.first()
        response = self.client.post(
            url,
            {
                "old_password" : user.password,
                "new_password" : new_password
            }
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_password, user.password)

        
class UserDeleteTestCase(BaseWithClientCredentialsTestCase):
    """
    Only superuser, or self (user) can delete a user record. 
    """
    def create_to_delete_user(self):
        to_delete_user = User.objects.create(
            email="delete@gmail.com",
            password="delete me"
        )
        return to_delete_user        

    def test_user_deletes_self(self):
        self.load_user_client_credentials()
        url = reverse('user-detail', kwargs={"pk":1}) # only one user created, thus pk=1
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_superuser_deletes_a_user(self):
        self.load_superuser_client_credentials()
        to_delete_user = self.create_to_delete_user()        
        url = reverse('user-detail', kwargs={"pk":to_delete_user.id})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)     

    def test_normal_user_deletes_another_user(self):
        self.load_user_client_credentials()
        to_delete_user = self.create_to_delete_user()      
        url = reverse('user-detail', kwargs={"pk":to_delete_user.id})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)    
    def test_unauthenticated_client_attempts_delete(self):
        to_delete_user = self.create_to_delete_user()            
        url = reverse('user-detail', kwargs={"pk":to_delete_user.id})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)          
