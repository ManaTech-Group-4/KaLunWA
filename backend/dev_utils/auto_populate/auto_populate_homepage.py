"""
    For Homepage
        - sample featured events
        - sample featured projects
        - sample news

exec(open("dev_utils/auto_populate/auto_populate_homepage.py").read())
"""

from kalunwa.content.models import (
    CampEnum,
    Event,
    Image,
    Jumbotron,
    News,
    Project,
) 
from django.utils import timezone


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

Jumbotron.objects.create(
    image= Image.objects.create(
        name = 'carousel image 5',
        image = 'images/content/carousel4.jpg'
    ),
    header_title = 'Extra Jumbo.',
    subtitle = "I am the 5th Jumbotron."
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
        image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
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
        image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
        is_featured=True,
    )

print('populated featured events & projects (General)')
#-------------------------------------------------------------------------------
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