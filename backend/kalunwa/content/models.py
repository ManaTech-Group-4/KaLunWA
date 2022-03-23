from datetime import datetime
from django.db import models
from django.forms import DateField
from kalunwa.core.models import TimestampedModel

class CampEnum(models.TextChoices):
    SUBA = 'SB', 'Suba'
    LASANG = 'LSNG', 'Lasang'
    BAYBAYON = 'BYBYN', 'Baybayon'
    ZEROWASTE = 'ZW', 'Zero Waste'
    GENERAL = 'GNRL', 'General'
    

class ContentModel(TimestampedModel):
    is_published = models.BooleanField(default=False)
    # created_by (User)
    # last_updated_by (User)

    class Meta:
        abstract=True


class Tag(ContentModel):
    name = models.CharField(db_index=True, unique=True, max_length=50)

    def __str__(self) -> str:
        return self.name


class Image(ContentModel):
    title = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/content/')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True) # blank=true allows 0 tags

    def __str__(self) -> str:
        return self.title


class Jumbotron(ContentModel):
    image = models.OneToOneField(Image,  related_name='jumbotrons', on_delete=models.PROTECT) 
    header_title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=225)

    def __str__(self) -> str:
        return f'{self.header_title} jumbotron'


class Event(ContentModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    image = models.OneToOneField(Image, related_name='events', on_delete=models.PROTECT) 
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
        

class Project(ContentModel):
    title = models.CharField(max_length=50)  
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    image = models.OneToOneField(Image, related_name='projects', on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class News(ContentModel):
    title = models.CharField(max_length=50)  
    description = models.TextField()
    image = models.OneToOneField(Image, related_name='news', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Announcement(ContentModel):
    title = models.CharField(max_length=50) 
    description = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.title