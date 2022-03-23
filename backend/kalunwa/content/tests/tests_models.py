
from django.test import TestCase
from django.utils import timezone
from kalunwa.content.models import Image, Jumbotron, Tag, Event, Project, News, Announcement, CampEnum #model class name
import tempfile

#https://docs.python.org/3/library/unittest.html 

class ModelTest(TestCase):

    def create_image_sample(self):
        newImage = tempfile.NamedTemporaryFile(suffix=".jpg", dir = 'media/images/content' ).name
        image_sample = Image.objects.create(title = "image_title", image=newImage)
        tag_sample = image_sample.tags.create(name="test_Tag")
        tag_sample.save()        
        return image_sample

    def test_tag_model(self):
        tag_model = Tag.objects.create(name="tag_title") #insert fields here
        self.assertTrue(isinstance(tag_model,Tag)) #if data goes db, return T 
        self.assertEqual(str(tag_model),"tag_title") #2 things are equal

    def test_image_model(self):
        image_model = self.create_image_sample()
        self.assertTrue(isinstance(image_model,Image)) 
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(str(image_model.tags.all()[0]), "test_Tag")
        self.assertEqual(str(image_model),"image_title")

    def test_jumbotron_model(self):
        jumbotron_model = Jumbotron.objects.create(
            featured_image=self.create_image_sample(), 
            header_title="jumbotron_title",
            short_description="jumbotron_description")
        self.assertTrue(isinstance(jumbotron_model,Jumbotron)) 
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(str(jumbotron_model),"jumbotron_title"+" jumbotron")

    def test_news_model(self):
        news_model = News.objects.create(
            title="news_title",
            description="news_description",
            featured_image=self.create_image_sample())
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(str(news_model),"news_title")

    def test_event_model(self):
        date_sample = timezone.now()
        event_model = Event.objects.create(
            title="event_title",
            description="event_description",
            start_date=date_sample,
            end_date=date_sample,
            camp=CampEnum.GENERAL.value,
            image=self.create_image_sample(),
            is_featured=False)
        self.assertTrue(isinstance(event_model,Event)) 
        self.assertEqual(str(event_model),"event_title")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(event_model.camp,CampEnum.GENERAL.value)
        self.assertFalse(event_model.is_featured)
        
    def test_project_model(self):
        date_sample = timezone.now()
        project_model = Project.objects.create(
            title="project_title",
            description="project_description",
            start_date=date_sample,
            end_date=date_sample,
            camp=CampEnum.GENERAL.value,
            image=self.create_image_sample(),
            is_featured=False)
        self.assertTrue(isinstance(project_model,Project)) 
        self.assertEqual(str(project_model),"project_title")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(project_model.camp,CampEnum.GENERAL.value)
        self.assertFalse(project_model.is_featured)

    def test_announcement_model(self):
        announcement_model = Announcement.objects.create(
            title="announcement_title", 
            description="announcement_description") 
        self.assertTrue(isinstance(announcement_model,Announcement)) 
        self.assertEqual(str(announcement_model),"announcement_title") 
