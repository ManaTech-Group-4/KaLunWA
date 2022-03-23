
from django.contrib.auth.models import User
from django.utils import timezone
from kalunwa.content.models import Image, Jumbotron, Event, CampEnum, News, Project


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
        title = 'carousel image 1',
        image = 'images/content/carousel1.jpg'
    ),
    header_title = 'Plant.',
    short_description = "Let's grow and foster together."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        title = 'carousel image 2',
        image = 'images/content/carousel2.jpg'
    ),
    header_title = 'Pursue.',
    short_description = "Onwards with a goal to achieve."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        title = 'carousel image 3',
        image = 'images/content/carousel3.jpg'
    ),
    header_title = 'Teamwork.',
    short_description = "Unity is the key."
)

Jumbotron.objects.create(
    image= Image.objects.create(
        title = 'carousel image 4',
        image = 'images/content/carousel4.jpg'
    ),
    header_title = 'Home.',
    short_description = "Sharing the warmth of family."
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
        title = f'event default {_}',
        image = 'images/content/event.jpg'
    )

    Event.objects.create(
        title= f'Event {_}', 
        description= f'description {_}',
        start_date=timezone.now(),
        end_date=timezone.now(),
        camp=CampEnum.GENERAL,
        image = Image.objects.get(title=f'event default {_}'),
        is_featured=True,        
    )

    # featured projects
    project_image = Image.objects.create(
        title = f'project default {_}',
        image = 'images/content/project.jpg'       
    ) 
    Project.objects.create(
        title= f'Project {_}', 
        description= f'description {_}',
        start_date=timezone.now(),
        end_date=timezone.now(),
        camp=CampEnum.GENERAL,
        image = Image.objects.get(title=f'project default {_}'),
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
        title = 'news image 1',
        image = 'images/content/news1.jpg'
    )
)

News.objects.create(
    title = 'News Headline 2',
    description= description,
    image = Image.objects.create(
        title = 'news image 2',
        image = 'images/content/news2.jpeg'
    )
)

News.objects.create(
    title = 'News Headline 3',
    description= description,
    image = Image.objects.create(
        title = 'news image 3',
        image = 'images/content/news3.jpg'
    )
)
print('populated news')
print('end of script')
