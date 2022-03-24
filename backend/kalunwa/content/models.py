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


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-----------------------------newly added models as of 23/3/2022-------------------------------------------------



class OfficerEnum(models.TextChoices):
    PRESIDENT = 'PR', 'President'
    VICE_PRESIDENT = 'VP', 'Vice-President'
    SECRETARY = 'SEC', 'Secretary'
    TREASURER = 'TRE', 'Treasurer'
    AUDITOR = 'AUD', 'Auditor'
    PIO = 'PIO', 'Public Information Officer'
    OVERSEER = 'OVRS', 'Overseer'
    BOARD_OF_TRUSTEES = 'BOR', 'Board of Trustees'
    CAMP_LEADER = 'CL', 'Camp Leader'
    OTHER = 'OTHR', 'Other'


class Demographics(AuthoredModel):
    location = models.CharField(max_length=50)
    member_count = models.IntegerField()

    def __str__(self) -> str:
        return self.location #what should i return???

class CampPage(AuthoredModel):
    name = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    description = models.TextField()
    image = models.OneToOneField(Image, related_name='camp', on_delete=models.PROTECT) #not sure with related_image should it be the specific camp?
    
    def __str__(self) -> str:
        return self.name #returns the 'key letters', should be name

class OfficerBase(AuthoredModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(choices=OfficerEnum.choices, max_length=9, default=OfficerEnum.OTHER)
    background = models.TextField()

    class Meta:
        abstract=True

class OrgLeader(OfficerBase):
    image = models.OneToOneField(Image, related_name='org_leader', on_delete=models.PROTECT) #or add in officerBase w/ related_name = officer for both orgleader&campOfficer

    def __str__(self) -> str:
        return self.last_name + ', ' + self.first_name #or should I just return the position

class CampOfficer(OfficerBase):
    motto = models.TextField()
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    image = models.OneToOneField(Image, related_name='camp_officer', on_delete=models.PROTECT)
 

    def __str__(self) -> str:
        return self.last_name + ', ' + self.first_name

