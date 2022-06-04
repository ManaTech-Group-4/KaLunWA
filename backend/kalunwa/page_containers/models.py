from django.db import models
from kalunwa.content.models import (
    Jumbotron,    
    Event,
    Project,
)
from kalunwa.core.models import TimestampedModel

# Create your models here.
class PageContainer(TimestampedModel):
    name = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length = 255, null = True, blank = True, unique=True)
    # edited_by
    jumbotrons = models.ManyToManyField(Jumbotron, through='PageContainedJumbotron')
    events = models.ManyToManyField(Event, through='PageContainedEvent')    
    projects = models.ManyToManyField(Project, through='PageContainedProject')        


class PageContainedJumbotron(models.Model):
    container = models.ForeignKey(PageContainer, on_delete=models.CASCADE) 
    jumbotron = models.ForeignKey(Jumbotron, on_delete=models.CASCADE)
    section_order = models.IntegerField()
    class Meta:
        # avoid duplicates when using update_or_create
        constraints = [
                    models.UniqueConstraint(
                        fields= ['container', 'jumbotron', 'section_order'],
                        name='unique_container_jumbo_order'),
        # container should only have 1 jumbotron at a position/order  
                    models.UniqueConstraint(
                        fields= ['container', 'section_order'],
                        name='unique_container_order_for_contained_jumbotron'),
        # container should have unique jumbotrons                        
                    models.UniqueConstraint(
                        fields= ['container', 'jumbotron'],
                        name='unique_container_jumbotron'),                        
                ]        


class PageContainedEvent(models.Model):
    container = models.ForeignKey(PageContainer, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    section_order = models.IntegerField()
    class Meta:
        # avoid duplicates when using update_or_create
        constraints = [
                    models.UniqueConstraint(
                        fields= ['container', 'event', 'section_order'],
                        name='unique_container_event_order'),
        # container should only have 1 jumbotron at a position/order  
                    models.UniqueConstraint(
                        fields= ['container', 'section_order'],
                        name='unique_container_order_for_contained_event'),
        # container should have unique jumbotrons                        
                    models.UniqueConstraint(
                        fields= ['container', 'event'],
                        name='unique_container_event'),                        
                ]              

class PageContainedProject(models.Model):
    container = models.ForeignKey(PageContainer, on_delete=models.CASCADE) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    section_order = models.IntegerField()
    class Meta:
        # avoid duplicates when using update_or_create
        constraints = [
                    models.UniqueConstraint(
                        fields= ['container', 'project', 'section_order'],
                        name='unique_container_project_order'),
        # container should only have 1 jumbotron at a position/order  
                    models.UniqueConstraint(
                        fields= ['container', 'section_order'],
                        name='unique_container_order_for_contained_project'),
        # container should have unique jumbotrons                        
                    models.UniqueConstraint(
                        fields= ['container', 'project'],
                        name='unique_container_project'),                        
                ]     


