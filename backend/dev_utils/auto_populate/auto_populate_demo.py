
from django.contrib.auth.models import User
from django.utils import timezone
from kalunwa.content.models import CampLeader, Image, Jumbotron, Event, CampEnum, News, Project, CampPage, Demographics, OrgLeader


"""
Auto-populates database for sprint review.
Prepare sample data for demo or trials on retrieving data.
Makes database deletable and buildable during complications in dev.

current generatable content:
    - superuser (user:admin, pass: admin123)
    - sample jumbotrons
    - sample featured events
    - sample featured projects
    - sample news

requirements:
    - file names must be accurate and should be in the specified directory
         (see fields with directories e.g. images/content/...jpg)
        - will temporarily upload files to repo in its dedicated directory
            to avoid files not being found

    - as much as possible, an empty database 
        (or at least check for conflicts, then comment out object creations)

        if db is deleted, do command before running the script:

            python manage.py migrate

                - applies the actual changes on the database 
                (assuming migration files are correct, it'll go well)

            note: Migration files are a compilation of the requirements/changes
                done in the (coded) data models. 
        
            note: if deleting db raises Error: 'Resource busy', 
                try:
                    close the interactive shell in the terminal & try again.
                    close sqlite & try again.
                    stop django server & try again. 
            

to populate database, run the script ONCE:
- in cmd (backend directory), do

    python manage.py shell
            - this opens the interactive python shell. Then enter  
    
    exec(open("dev_utils/auto_populate/auto_populate_demo.py").read())    
"""

#-------------------------------------------------------------------------------
# create superuser
superuser = User.objects.create_user('admin', password='admin123')     
superuser.is_superuser=True
superuser.is_staff=True
superuser.save()
print('populated superuser')
#-------------------------------------------------------------------------------
# create sample jumbotrons
Jumbotron.objects.create(
    image= Image.objects.create(
        name = 'carousel image 1',
        image = 'images/content/carousel1.jpg'
    ),
    header_title = 'Plant.',
    subtitle = "Let's grow and foster together."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        name = 'carousel image 2',
        image = 'images/content/carousel2.jpg'
    ),
    header_title = 'Pursue.',
    subtitle = "Onwards with a goal to achieve."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        name = 'carousel image 3',
        image = 'images/content/carousel3.jpg'
    ),
    header_title = 'Teamwork.',
    subtitle = "Unity is the key."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        name = 'carousel image 4',
        image = 'images/content/carousel4.jpg'
    ),
    header_title = 'Home.',
    subtitle = "Sharing the warmth of family."
)
print('populated homepage jumbotrons')
#-------------------------------------------------------------------------------
# create sample featured events, projects
"""
events are encoded without proper information to deliver bare minimum for homepage. 
revision needed when working on individual content pages (e.g. news, events)
"""

for _ in range(1,4): # to make primary keys (pk's) start at count 1
    # when image is made foreign key (not one to one), this block of code
    # can be moved outside this loop.
    # it's currently like this because an event can only have one Image instance.

    #events
    event_image = Image.objects.create(
        name = f'event default {_}',
        image = 'images/content/event.jpg'
    )

    Event.objects.create(
        title= f'Event {_}', 
        description= f'description {_}',
        start_date=timezone.now(),
        end_date=timezone.now(),
        camp=CampEnum.GENERAL,
        image = Image.objects.get(name=f'event default {_}'),
        is_featured=True,        
    )

    # featured projects
    project_image = Image.objects.create(
        name = f'project default {_}',
        image = 'images/content/project.jpg'       
    ) 
    Project.objects.create(
        title= f'Project {_}', 
        description= f'description {_}',
        start_date=timezone.now(),
        end_date=timezone.now(),
        camp=CampEnum.GENERAL,
        image = Image.objects.get(name=f'project default {_}'),
        is_featured=True,
    )
print('populated featured events & projects')
#-------------------------------------------------------------------------------
# news
description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco'

News.objects.create(
    title = f'News Headline 1',
    description=description ,
    image = Image.objects.create(
        name = 'news image 1',
        image = 'images/content/news1.jpg'
    )
)

News.objects.create(
    title = 'News Headline 2',
    description= description,
    image = Image.objects.create(
        name = 'news image 2',
        image = 'images/content/news2.jpeg'
    )
)

News.objects.create(
    title = 'News Headline 3',
    description= description,
    image = Image.objects.create(
        name = 'news image 3',
        image = 'images/content/news3.jpg'
    )
)
print('populated news')

#-------------------------------------------------------------------------------
# demographics

Demographics.objects.create(
    location = 'Tagbilaran',
    member_count = 40
)

Demographics.objects.create(
    location = 'Jagna',
    member_count = 30
)

Demographics.objects.create(
    location = 'Anda',
    member_count = 17
)
print('populated demographics')
#-------------------------------------------------------------------------------
# camps 

for _ in range(4):
    Image.objects.create(
        name = f'camp default {_}',
        image = 'images/content/event.jpg'
    )    

CampPage.objects.create(
    name=CampEnum.SUBA.value,
    description = 'default description',
    image = Image.objects.get(name='camp default 0')
)

CampPage.objects.create(
    name=CampEnum.BAYBAYON.value,
    description = 'default description',
    image = Image.objects.get(name='camp default 1')
)

CampPage.objects.create(
    name=CampEnum.ZEROWASTE.value,
    description = 'default description',
    image = Image.objects.get(name='camp default 2')
)

CampPage.objects.create(
    name=CampEnum.LASANG.value,
    description = 'default description',
    image = Image.objects.get(name='camp default 3')
)
print('populated camps')
#-------------------------------------------------------------------------------
# Leaders

################ Camp Leaders

for _ in range(4):
    dummy_image = Image.objects.create(
        name = f'camp leader {_}',
        image = 'images/content/event.jpg'
    )   

    CampLeader.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        background = f'background {_}',
        advocacy = f'advocacy {_}',
        position = CampLeader.Positions.LEADER,
        image=dummy_image
    )

camps = [CampEnum.BAYBAYON, CampEnum.SUBA, CampEnum.LASANG, CampEnum.ZEROWASTE]

# assigning respective camps, field is initially GNRL
for _ in range(4):
    current_leader = CampLeader.objects.get(pk=_+1)
    current_leader.camp = camps[_] # 0-3
    current_leader.save()

print('populated Camp leaders')

################ Org Leaders (Execom, Directors)

dummy_image = Image.objects.create(
    name = f'camp leader {_}',
    image = 'images/content/event.jpg'
)
    # President
OrgLeader.objects.create(
    first_name = 'Jairus',
    last_name = 'Chiu',
    background = 'background',
    advocacy = 'advocacy',
    position = OrgLeader.Positions.PRESIDENT,

    image=Image.objects.create(
        name = f'pres',
        image = 'images/content/event.jpg'
    )
)
    # Vice President
OrgLeader.objects.create(
    first_name = 'Vice',
    last_name = 'Pres',
    background = 'background',
    advocacy = 'advocacy',
    position = OrgLeader.Positions.VICE_PRESIDENT,
    
    image=Image.objects.create(
        name = 'vpres',
        image = 'images/content/event.jpg'
    )
)

    # Secretary
OrgLeader.objects.create(
    first_name = 'Sec',
    last_name = 'Retary',
    background = 'background',
    advocacy = 'advocacy',
    position = OrgLeader.Positions.SECRETARY,
    
    image=Image.objects.create(
        name = 'secretary',
        image = 'images/content/event.jpg'
    )
)

    # Treasurer
OrgLeader.objects.create(
    first_name = 'Tre',
    last_name = 'Asurer',
    background = 'background',
    advocacy = 'advocacy',
    position = OrgLeader.Positions.TREASURER,
    
    image=Image.objects.create(
        name = 'treasurer',
        image = 'images/content/event.jpg'
    )
)

    # Auditor
OrgLeader.objects.create(
    first_name = 'Audi',
    last_name = 'Tor',
    background = 'background',
    advocacy = 'advocacy',
    position = OrgLeader.Positions.AUDITOR,
    
    image=Image.objects.create(
        name = 'auditor',
        image = 'images/content/event.jpg'
    )
)
    
print('populated Org Leaders (5 highest ranks)')

print('end of script')


# exec(open("dev_utils/auto_populate/auto_populate_demo.py").read())
