from django.db import models

# Create your models here.
from django.db import models
from kalunwa.core.models import TimestampedModel


class ContentModel(TimestampedModel):
    is_published = (models.BooleanField)
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
    image = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True) # warning for image tag, 0 to many tags

    def __str__(self) -> str:
        return self.title

class Jumbotron(ContentModel):
    # featured_image
    # header_title
    # short_description
    pass

class Homepage(ContentModel):
    # fk - jumbotron
    # fk - featured event
    # fk - featured project
    pass

class Event(ContentModel):
    # title
    # description
    # start_date
    # end_date
    # camp
    # featured_image
    #status
    pass

class Project(ContentModel):
    # title
    # description
    # start_date
    # end_date
    # camp
    # featured_image
    #status    
    pass

class News(ContentModel):
    # title
    # description
    #featured_image
    pass

class Announcement(ContentModel):
    # title
    # description
    pass
