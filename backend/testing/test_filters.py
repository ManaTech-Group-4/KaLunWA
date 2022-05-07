
from kalunwa.content.models import Image, CampEnum, Commissioner,CabinOfficer, CampLeader, OrgLeader, CampPage
from .utils import get_test_image_file
from rest_framework.test import APITestCase

class CampNameInFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()
    
        for _ in range(4):   
            CampPage.objects.create(
                name=CampEnum.values[_],
                description = f'description {_}', 
                image = Image.objects.create(name=f'image_{_}', image=cls.image_file),
                gallery = Image.objects.get(pk=_),
        ) 


class OrgLeaderPositionFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(9): 
            OrgLeader.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            position = OrgLeader.Positions.values[_]
            )           

        cls.orgleaders_count = len(OrgLeader.objects.all())   

    def test_correct_position_input(self): #all positions tested
        positions = ['President','Vice-President','Secretary','Treasurer','Auditor', 'Public Information Officer', 'Overseer', 'Director','Other']
        for position in positions:
            response = self.client.get(f'/api/orgleaders/?position={position}')       
            self.assertEqual(len(response.data), 1) 
    def test_execomm_camp_input(self):
        position = 'ExeComm'
        response = self.client.get(f'/api/orgleaders/?position={position}')        
        self.assertEqual(len(response.data), 7)  
    def test_none_camp_value_input(self):
        positions = [0, 'aaa', '@!*']
        for position in positions:
            response = self.client.get(f'/api/orgleaders/?position={position}')    
            self.assertEqual(len(response.data), 0) 
    def test_none_camp_input(self):
        response = self.client.get(f'/api/orgleaders/?')       
        self.assertEqual(len(response.data), self.orgleaders_count)  


class CampFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(3): 
            CampLeader.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            camp = CampEnum.values[_],
            position = CampLeader.Positions.values[_],
            motto = f'motto {_}'
            )           

        cls.campleader_count = len(CampLeader.objects.all())   

    def test_correct_camp_input(self): #not all camps were tested since position index will be out of range
        camps = ['Suba','Lasang','Baybayon']
        for camp in camps:
            response = self.client.get(f'/api/campleaders/?camp={camp}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_camp_value_input(self):
        camps = [0, 'aaa', '@!*']
        for camp in camps:
            response = self.client.get(f'/api/campleaders/?camp={camp}')      
            self.assertEqual(len(response.data), 0) 
    def test_none_camp_input(self):
        response = self.client.get(f'/api/campleaders/?')       
        self.assertEqual(len(response.data), self.campleader_count)  


class CabinOfficerCategoryFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(4): 
            CabinOfficer.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            camp = CampEnum.values[_],
            category = CabinOfficer.Categories.values[_],
            position = CabinOfficer.Positions.values[_]
            )           

        cls.cabinofficer_count = len(CabinOfficer.objects.all())   

    def test_correct_category_input(self): #not all categories were tested since position index will be out of range
        categories = ['Secretariat Cabin','Finance Cabin','Ways and Means Cabin','Publicity Cabin']
        for category in categories:
            response = self.client.get(f'/api/cabinofficers/?category={category}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_category_value_input(self):
        categories = [0, 'aaa', '@!*']
        for category in categories:
            response = self.client.get(f'/api/cabinofficers/?category={category}')       
            self.assertEqual(len(response.data), 0) 
    def test_none_category_input(self):
        response = self.client.get(f'/api/cabinofficers/?')       
        self.assertEqual(len(response.data), self.cabinofficer_count)  


class CommissionerCategoryFilterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.image_file = get_test_image_file()

        for _ in range(3): 
            Commissioner.objects.create(
            first_name = f'first_name {_}', 
            last_name = f'last_name {_}',
            quote = f'quote {_}',
            image = Image.objects.create(name=f'image_{_}', image=cls.image_file),  
            category = Commissioner.Categories.values[_],
            position = Commissioner.Positions.values[_]
            )           

        cls.commissioner_count = len(Commissioner.objects.all())   

    def test_correct_category_input(self): #all category tested
        categories = ['Election','Grievance and Ethics','Other']
        for category in categories:
            response = self.client.get(f'/api/commissioners/?category={category}')       
            self.assertEqual(len(response.data), 1) 
    def test_none_category_value_input(self):
        categories = [0, 'aaa', '@!*']
        for category in categories:
            response = self.client.get(f'/api/commissioners/?category={category}')       
            self.assertEqual(len(response.data), 0)  
    def test_none_category_input(self):
        response = self.client.get(f'/api/commissioners/?')       
        self.assertEqual(len(response.data), self.commissioner_count)  

