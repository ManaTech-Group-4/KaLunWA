from django.test import TestCase
from django.utils import timezone
from kalunwa.content.models import Image, Jumbotron, Tag, Event, Project, News, Announcement, CampEnum
from kalunwa.content.models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer, Contributor
import tempfile


class ModelTest(TestCase):

    def create_image_sample(self):
        newImage = tempfile.NamedTemporaryFile(suffix=".jpg", dir = 'media/images/content' ).name
        image_sample = Image.objects.create(name = "image_title", image=newImage)
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
        self.assertEqual(str(image_model),f'{image_model.id}. image_title')


    def test_jumbotron_model(self):
        jumbotron_model = Jumbotron.objects.create(
            image=self.create_image_sample(), 
            header_title="jumbotron_title",
            subtitle="jumbotron_description")
        self.assertTrue(isinstance(jumbotron_model,Jumbotron)) 
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(str(jumbotron_model),f'{jumbotron_model.header_title} jumbotron')


    def test_news_model(self):
        news_model = News.objects.create(
            is_published = True,
            title="news_title",
            description="news_description",
            image=self.create_image_sample())
        self.assertEqual(Image.objects.count(), 1)
        self.assertTrue(news_model.is_published)
        self.assertEqual(str(news_model),"news_title")
        

    def test_announcement_model(self):
        announcement_model = Announcement.objects.create(
            is_published = True,
            title="announcement_title", 
            description="announcement_description") 
        self.assertTrue(isinstance(announcement_model,Announcement)) 
        self.assertTrue(announcement_model.is_published)
        self.assertEqual(str(announcement_model),"announcement_title") 


    def test_event_model(self):
        date_sample = timezone.now()
        event_model = Event.objects.create(
            is_published = True,
            title="event_title",
            description="event_description",
            start_date=date_sample,
            end_date=date_sample,
            camp=CampEnum.GENERAL,
            image=self.create_image_sample(),
            is_featured=False)
        self.assertTrue(isinstance(event_model,Event)) 
        self.assertTrue(event_model.is_published)
        self.assertEqual(str(event_model),"event_title")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(event_model.camp,"GNRL")
        self.assertFalse(event_model.is_featured)


    def test_project_model(self):
        date_sample = timezone.now()
        project_model = Project.objects.create(
            is_published = True,
            title="project_title",
            description="project_description",
            start_date=date_sample,
            end_date=date_sample,
            camp=CampEnum.GENERAL,
            image=self.create_image_sample(),
            is_featured=False)
        self.assertTrue(isinstance(project_model,Project)) 
        self.assertTrue(project_model.is_published)
        self.assertEqual(str(project_model),"project_title")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(project_model.camp,"GNRL")
        self.assertFalse(project_model.is_featured)
    

    def test_demographics_model(self):
        demographics_model = Demographics.objects.create(
            location = "sample_location",
            member_count = 20)
        self.assertTrue(isinstance(demographics_model,Demographics))
        self.assertEqual(str(demographics_model),"sample_location") 
        self.assertEqual(demographics_model.member_count,20)
    

    def test_camp_page_model(self):
        camp_page_model = CampPage.objects.create(
            name = CampEnum.GENERAL,
            description = "camp_page_description",
            image=self.create_image_sample(),)
        self.assertTrue(isinstance(camp_page_model,CampPage))
        self.assertEqual(str(camp_page_model),CampEnum.GENERAL.label) 
        self.assertEqual(camp_page_model.description,"camp_page_description")
        self.assertEqual(Image.objects.count(), 1)


    def test_org_leader_model(self):
        org_leader_model = OrgLeader.objects.create(
            first_name = "leader_first_name",
            last_name = "leader_last_name",
            quote = "leader_quote",
            image=self.create_image_sample(),
            position = OrgLeader.Positions.OTHER)
        self.assertTrue(isinstance(org_leader_model,OrgLeader))
        self.assertEqual(org_leader_model.first_name,"leader_first_name")
        self.assertEqual(org_leader_model.last_name,"leader_last_name")
        self.assertEqual(org_leader_model.quote,"leader_quote")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(org_leader_model.position, OrgLeader.Positions.OTHER)
        self.assertEqual(org_leader_model.get_position(), OrgLeader.Positions.OTHER.label)
        self.assertEqual(str(org_leader_model),f'{OrgLeader.Positions.OTHER.label} : {org_leader_model.last_name}')
        

    def test_commissioner_model(self):
        commissioner_model = Commissioner.objects.create(
            first_name = "commissioner_first_name",
            last_name = "commissioner_last_name",
            quote = "commissioner_quote",
            image=self.create_image_sample(),
            category = Commissioner.Categories.OTHER,
            position = Commissioner.Positions.OTHER)
        self.assertTrue(isinstance(commissioner_model,Commissioner))
        self.assertEqual(commissioner_model.first_name,"commissioner_first_name")
        self.assertEqual(commissioner_model.last_name,"commissioner_last_name")
        self.assertEqual(commissioner_model.quote,"commissioner_quote")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(commissioner_model.category, Commissioner.Categories.OTHER)
        self.assertEqual(commissioner_model.position, Commissioner.Positions.OTHER)
        self.assertEqual(commissioner_model.get_position(), Commissioner.Positions.OTHER.label)
        self.assertEqual(commissioner_model.get_category(), Commissioner.Categories.OTHER.label)
        self.assertEqual(str(commissioner_model),f'{Commissioner.Categories.OTHER.label} {Commissioner.Positions.OTHER.label}: {commissioner_model.last_name}')


    def test_camp_leader_model(self):
        camp_leader_model = CampLeader.objects.create(
            first_name = "camp_leader_first_name",
            last_name = "camp_leader_last_name",
            quote = "camp_leader_quote",
            image=self.create_image_sample(),
            camp = CampEnum.GENERAL,
            position = Commissioner.Positions.OTHER,
            motto = "camp_leader_motto")
        self.assertTrue(isinstance(camp_leader_model,CampLeader))
        self.assertEqual(camp_leader_model.first_name,"camp_leader_first_name")
        self.assertEqual(camp_leader_model.last_name,"camp_leader_last_name")
        self.assertEqual(camp_leader_model.quote,"camp_leader_quote")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(camp_leader_model.camp, CampEnum.GENERAL)
        self.assertEqual(camp_leader_model.position, CampLeader.Positions.OTHER)
        self.assertEqual(camp_leader_model.motto,"camp_leader_motto")
        self.assertEqual(camp_leader_model.get_position(), CampLeader.Positions.OTHER.label)
        self.assertEqual(camp_leader_model.get_camp(), CampEnum.GENERAL.label)
        self.assertEqual(str(camp_leader_model),f'Camp {CampEnum.GENERAL.label}, {CampLeader.Positions.OTHER.label}: {camp_leader_model.last_name}')        


    def test_cabin_officer_model(self):
        cabin_officer_model = CabinOfficer.objects.create(
            first_name = "cabin_officer_first_name",
            last_name = "cabin_officer_last_name",
            quote = "cabin_officer_quote",
            image=self.create_image_sample(),
            camp = CampEnum.GENERAL,
            category = CabinOfficer.Categories.OTHER,
            position = CabinOfficer.Positions.OTHER)
        self.assertTrue(isinstance(cabin_officer_model,CabinOfficer))
        self.assertEqual(cabin_officer_model.first_name,"cabin_officer_first_name")
        self.assertEqual(cabin_officer_model.last_name,"cabin_officer_last_name")
        self.assertEqual(cabin_officer_model.quote,"cabin_officer_quote")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(cabin_officer_model.camp, CampEnum.GENERAL)
        self.assertEqual(cabin_officer_model.category, CabinOfficer.Categories.OTHER)
        self.assertEqual(cabin_officer_model.position, CabinOfficer.Positions.OTHER)
        self.assertEqual(cabin_officer_model.get_position(), CabinOfficer.Positions.OTHER.label)
        self.assertEqual(cabin_officer_model.get_camp(), CampEnum.GENERAL.label)
        self.assertEqual(cabin_officer_model.get_category(), CabinOfficer.Categories.OTHER.label)
        self.assertEqual(str(cabin_officer_model),f'Camp {CampEnum.GENERAL.label} {CabinOfficer.Categories.OTHER.label}, {CabinOfficer.Positions.OTHER.label}: {cabin_officer_model.last_name}')            

    def test_contributor_model(self):
        contributor_model = Contributor.objects.create(
            name = "contributor_name",
            image=self.create_image_sample(),
            category = Contributor.Categories.OTHER)
        self.assertTrue(isinstance(contributor_model,Contributor))
        self.assertEqual(contributor_model.name,"contributor_name")
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(contributor_model.category, Contributor.Categories.OTHER)
        self.assertEqual(contributor_model.get_category(), Contributor.Categories.OTHER.label)
        self.assertEqual(str(contributor_model),f'{Contributor.Categories.OTHER.label}: {contributor_model.name}')
        
