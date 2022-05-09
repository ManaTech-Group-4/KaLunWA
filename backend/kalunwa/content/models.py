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

    class Meta(TimestampedModel.Meta):
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
        return str(self.id) + '. ' + self.name


class Jumbotron(AuthoredModel):
    header_title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=225)
    is_featured = models.BooleanField(default=False)    
    image = models.OneToOneField(Image,  related_name='jumbotrons', on_delete=models.PROTECT) 

    def __str__(self) -> str:
        return f'{self.header_title} jumbotron'


class ContentBase(AuthoredModel):
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta(AuthoredModel.Meta):
        abstract=True


class News(ContentBase):
    image = models.OneToOneField(Image, related_name='news', on_delete=models.PROTECT, default =' ')

    def __str__(self) -> str:
        return self.title


class Announcement(ContentBase):
    meta_description = models.CharField(max_length=225)
    def __str__(self) -> str:
        return self.title


class Event(ContentBase):
    image = models.OneToOneField(Image, related_name='events', on_delete=models.PROTECT) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    is_featured = models.BooleanField(default=False)
    gallery = models.ManyToManyField(Image, related_name='gallery_events', blank=True)
    contributors = models.ManyToManyField('content.Contributor', related_name='events', blank=True)

    def __str__(self) -> str:
        return self.title

    def get_camp(self):
        return f'{self.get_camp_display()}'       


class Project(ContentBase):
    image = models.OneToOneField(Image, related_name='projects', on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    is_featured = models.BooleanField(default=False)
    gallery = models.ManyToManyField(Image, related_name='gallery_projects', blank=True)
    contributors = models.ManyToManyField('content.Contributor', related_name='projects', blank=True)

    def __str__(self) -> str:
        return self.title

    def get_camp(self):
        return f'{self.get_camp_display()}'        


class Demographics(AuthoredModel):
    location = models.CharField(max_length=50)
    member_count = models.IntegerField()

    def __str__(self) -> str:
        return self.location 


class CampPage(AuthoredModel):
    name = models.CharField(choices=CampEnum.choices, max_length=5, unique=True)
    tagline = models.CharField(max_length=225)
    description = models.TextField()
    image = models.OneToOneField(Image, related_name='camp', on_delete=models.PROTECT) 
    gallery = models.ManyToManyField(Image, related_name='gallery_camps', blank=True)

    def __str__(self) -> str:
        return self.get_name_display()

    def get_name(self):
        return f'{self.get_name_display()}'


class LeaderBase(AuthoredModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    quote = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.PROTECT)

    class Meta:
        abstract=True
    
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_position(self):
        return f'{self.get_position_display()}'

class OrgLeader(LeaderBase): # how to make pres -> overseer unique
    class Positions(models.TextChoices):
        PRESIDENT = 'PR', 'President'
        VICE_PRESIDENT = 'VP', 'Vice-President'
        SECRETARY = 'SEC', 'Secretary'
        TREASURER = 'TRE', 'Treasurer'
        AUDITOR = 'AUD', 'Auditor'
        PIO = 'PIO', 'Public Information Officer'
        OVERSEER = 'OVRS', 'Overseer'
        DIRECTOR = 'DIR', 'Director'
        OTHER = 'OTHR', 'Other'

    position = models.CharField(choices=Positions.choices, max_length=5, default=Positions.OTHER)


    def __str__(self) -> str:
        return f'{self.get_position_display()} : {self.last_name}'  


class Commissioner(LeaderBase):
    class Categories(models.TextChoices):
        ELECTION = 'ELCT', 'Election'
        GRIEVANCE_AND_ETHICS = 'GAE', 'Grievance and Ethics'
        OTHER = 'OTHR', 'Other'    

    class Positions(models.TextChoices):
        CHIEF = 'CHF', 'Chief Commissioner'
        COMMISSIONER = 'CMSR', 'Commissioner'
        OTHER = 'OTHR', 'Other'        

    category = models.CharField(choices=Categories.choices, max_length=5, default=Categories.OTHER)
    position = models.CharField(choices=Positions.choices, max_length=5, default=Positions.OTHER)


    def __str__(self) -> str:
        return f'{self.get_category_display()} {self.get_position_display()}: {self.last_name}'
        # e.g. Election Chief Commissioner: Junel 

    def get_category(self):
        return f'{self.get_category_display()}'             


class CampLeader(LeaderBase):
    class Positions(models.TextChoices):
        LEADER = 'LDR', 'Camp Leader'
        ASSISTANT_LEADER = 'ALDR', 'Assistant Camp Leader'
        OTHER = 'OTHR', 'Other'    

    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    position = models.CharField(choices=Positions.choices, max_length=5, default=Positions.OTHER)
    motto = models.TextField()

    def __str__(self) -> str:
        return f'Camp {self.get_camp_display()}, {self.get_position_display()}: {self.last_name}'
        # e.g. Camp Suba, Camp Leader: Junel  

    def get_camp(self):
        return f'{self.get_camp_display()}'    


class CabinOfficer(LeaderBase):
    class Positions(models.TextChoices):
        HEAD = 'HD', 'Cabin Head'
        ASSISTANT_HEAD = 'AHD', 'Assistant Cabin Head'
        SCRIBE = 'SCRB', 'Scribe'
        OTHER = 'OTHR', 'Other'

    class Categories(models.TextChoices):
        SECRETARIAT = 'SCRT', 'Secretariat Cabin'
        FINANCES = 'FNC', 'Finance Cabin'
        WAYS_AND_MEANS = 'WAM', 'Ways and Means Cabin'
        PUBLICITY = 'PBL', 'Publicity Cabin'
        PROGRAMS = 'PRG', 'Programs Cabin'
        RESEARCH = 'RSR', 'Research Cabin'
        OTHER = 'OTHR', 'Other'
        
    camp = models.CharField(choices=CampEnum.choices, max_length=5, default=CampEnum.GENERAL)
    category = models.CharField(choices=Categories.choices, max_length=5, default=Categories.OTHER)
    position = models.CharField(choices=Positions.choices, max_length=5, default=Positions.OTHER)

    def __str__(self) -> str:
        return f'Camp {self.get_camp_display()} {self.get_category_display()}, {self.get_position_display()}: {self.last_name}'
        # e.g. Camp Suba Secretariat Cabin, Cabin Head: Junel  
    def get_camp(self):
        return f'{self.get_camp_display()}'

    def get_category(self):
        return f'{self.get_category_display()}'     


class Contributor(models.Model):
    class Categories(models.TextChoices):
        SPONSOR = 'SR', 'Sponsor'
        PARTNER = 'PR', 'Partner'
        OTHER = 'OTHR', 'Other'        
    name = models.CharField(max_length=100)
    image = models.OneToOneField(Image, related_name='contributors', on_delete=models.PROTECT)
    category = models.CharField(choices=Categories.choices, max_length=4, default=Categories.OTHER)

    def __str__(self) -> str:
        return f'{self.get_category_display()}: {self.name}'
        
    def get_category(self):
        return f'{self.get_category_display()}'        