from django.db import models
from kalunwa.content.models import (
    Jumbotron,    
    Event,
    Project,
)
from kalunwa.core.models import TimestampedModel

######
from django.db import IntegrityError
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
######


# Create your models here.
class PageContainer(TimestampedModel):
    name = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length = 255, null = True, blank = True, unique=True)
    # edited_by
    jumbotrons = models.ManyToManyField(Jumbotron, through='PageContainedJumbotron')
#     events = models.ManyToManyField(Event, through='PageContainedEvents')  
#     projects = models.ManyToManyField(Project, through='PageContainedProjects')        

   # flexible to put constraints on serializer validator .. 
        # if name=='homepage'
            # unique_container_and_jumbotron
                # for every homepageJumbotron, only 1 should be at position 1, etc. 
            # unique_container_and_order
                # for every homepageJumbotron, event should not be repeated


class PageContainedJumbotron(models.Model):
    container = models.ForeignKey(PageContainer, on_delete=models.CASCADE) 
    jumbotron = models.ForeignKey(Jumbotron, on_delete=models.CASCADE)
    section_order = models.IntegerField()
    # class Meta:
        # avoid duplicates when using update_or_create
        # unique_together = ('container', 'jumbotron', 'section_order')            
        # container should only have 1 jumbotron at a position/order        
        # unique_together = ('container', 'section_order') 
        # container should have unique jumbotrons
        # unique_together = ('container', 'jumbotron')            

# class PageContainedEvents(models.Model):
#     container = models.ForeignKey(PageContainer, on_delete=models.CASCADE) 
#     jumbotron = models.ForeignKey(Event, on_delete=models.CASCADE)
#     section_order = models.IntegerField()


