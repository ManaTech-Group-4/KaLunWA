from django.db import models
from kalunwa.core.models import TimestampedModel


class CampEnum(models.TextChoices):
    SUBA = 'SB', 'Suba'
    LASANG = 'LSNG', 'Lasang'
    BAYBAYON = 'BYBYN', 'Baybayon'
    ZEROWASTE = 'ZW', 'Zero Waste'
    GENERAL = 'GNRL', 'General'
    

class AuthoredModel(TimestampedModel):
    # created_by (User)
    # last_updated_by (User)

    class Meta:
        abstract=True


class Tag(AuthoredModel):
    name = models.CharField(db_index=True, unique=True, max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Image(AuthoredModel):
    name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/content/')
    tags = models.ManyToManyField(Tag, related_name='images', blank=True) # blank=true allows 0 tags

    def __str__(self) -> str:
        return self.name


class Jumbotron(AuthoredModel):
    header_title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=225)
    image = models.OneToOneField(Image,  related_name='jumbotrons', on_delete=models.PROTECT) 

    def __str__(self) -> str:
        return f'{self.header_title} jumbotron'


class ContentBase(AuthoredModel):
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        abstract=True

class News(ContentBase):
    image = models.OneToOneField(Image, related_name='news', on_delete=models.PROTECT, default =' ')

    def __str__(self) -> str:
        return self.title


class Announcement(ContentBase):
    def __str__(self) -> str:
        return self.title


class Event(ContentBase):
    image = models.OneToOneField(Image, related_name='events', on_delete=models.PROTECT) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
        

class Project(ContentBase):
    image = models.OneToOneField(Image, related_name='projects', on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


