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


class OrgLeaderEnum(models.TextChoices):
    PRESIDENT = 'PR', 'President'
    VICE_PRESIDENT = 'VP', 'Vice-President'
    SECRETARY = 'SEC', 'Secretary'
    TREASURER = 'TRE', 'Treasurer'
    AUDITOR = 'AUD', 'Auditor'
    PIO = 'PIO', 'Public Information Officer'
    OVERSEER = 'OVRS', 'Overseer'
    DIRECTOR = 'DIR', 'Director'
    OTHER = 'OTHR', 'Other'

class CommissionEnum(models.TextChoices):
    CHIEF = 'CHF', 'Chief Commissioner'
    COMMISSIONER = 'CMSR', 'Commissioner'
    OTHER = 'OTHR', 'Other'

class CommissionCategEnum(models.TextChoices):
    ELECTION = 'ELCT', 'Chief Commissioner'
    GRIEVANCE_AND_ETHICS = 'GAE', 'Grievance and Ethics'
    OTHER = 'OTHR', 'Other'

class CampLeaderEnum(models.TextChoices):
    LEADER = 'LDR', 'Camp Leader'
    ASSISTANT_LEADER = 'ALDR', 'Assistant Camp Leader'
    OTHER = 'OTHR', 'Other'

class CabinOfficerEnum(models.TextChoices):
    HEAD = 'HD', 'Cabin Head'
    ASSISTANT_HEAD = 'AHD', 'Assistant Cabin Head'
    SCRIBE = 'SCRB', 'Scribe'
    OTHER = 'OTHR', 'Other'

class CabinCategEnum(models.TextChoices):
    SECRETARIAT = 'SCRT', 'Secretariat Cabin'
    FINANCES = 'FNC', 'Finance Cabin'
    WAYS_AND_MEANS = 'WAM', 'Ways and Means Cabin'
    PUBLICITY = 'PBL', 'Publicity Cabin'
    PROGRAMS = 'PRG', 'Programs Cabin'
    RESEARCH = 'RSR', 'Research Cabin'
    OTHER = 'OTHR', 'Other'


class LeaderBase(AuthoredModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    background = models.TextField()
    advocacy = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.PROTECT)

    class Meta:
        abstract=True

class OrgLeader(LeaderBase):
    position = models.CharField(choices=OrgLeaderEnum.choices, max_length=5, default=OrgLeaderEnum.OTHER)
    def __str__(self) -> str:
        self.find_enum()
        return self.position + ' : ' + self.last_name


class Commissioner(LeaderBase):
    category = models.CharField(choices=CommissionCategEnum.choices, max_length=5, default=CommissionCategEnum.OTHER)
    position = models.CharField(choices=CommissionEnum.choices, max_length=5, default=CommissionEnum.OTHER)

    def __str__(self) -> str:
        return '(' + self.category + ') ' + self.position + ' : ' + self.last_name


class CampLeader(LeaderBase):
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    position = models.CharField(choices=CampLeaderEnum.choices, max_length=5, default=CampLeaderEnum.OTHER)
    motto = models.TextField()

    def __str__(self) -> str:
        return '(Camp: ' + self.camp + ') ' + self.position + ' : ' + self.last_name


class CabinOfficer(LeaderBase):
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    category = models.CharField(choices=CabinCategEnum.choices, max_length=5, default=CabinCategEnum.OTHER)
    position = models.CharField(choices=CabinOfficerEnum.choices, max_length=5, default=CabinOfficerEnum.OTHER)


    def __str__(self) -> str:
        return '(Camp: ' + self.camp + ') ' + self.position + ' : ' + self.last_name

#serializer logic to enums onetoone

#content
#add serializer
#add admin
#add views
#add url


#testing
#models
#url
#api

#auto_populate



#camp must be used only once in Camp Page or must be ready made
#combine all leaders? or not


#https://stackoverflow.com/questions/4143886/django-admin-disable-the-add-action-for-a-specific-model 