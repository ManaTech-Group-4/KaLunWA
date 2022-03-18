from django.test import TestCase
from kalunwa.content.models import Announcement
from django.utils import timezone

class AnnouncementModelTest(TestCase):
    def setUp(self):
            self.announcement = Announcement.objects.create(
                title='A1',
                description="A1 description",
                created_at=timezone.now(),
                updated_at=timezone.now(),
                is_published=True)

    
    def test_announcement_model(self):
            a = self.announcement
            self.assertTrue(isinstance(a, Announcement))
            self.assertEqual(str(a), 'A1')








#--------------------------------------------------------------
# python manage.py test kalunwa.content.tests.models
# coverage run manage.py test kalunwa.content.tests.test_models            


