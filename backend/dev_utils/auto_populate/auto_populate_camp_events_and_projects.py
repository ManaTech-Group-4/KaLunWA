"""
actual camp events and projects
    - some are still not final; see line comments

exec(open("dev_utils/auto_populate/auto_populate_camp_events_and_projects.py").read())
"""
from django.utils import timezone
from kalunwa.content.models import (
    CampEnum,
    Event,
    Image,
    Project,
)

#-------------------------------------------------------------------------------
# actual camp events and projects
# Lasang
    #  Events

Event.objects.create(
    title=  'KINAADMAN: A Sunday Series', 
    description= "The major objective of Kinaadman is to provide information to the general public about the terrestrial environment of Bohol. This initiative is intended to eradicating Boholanos' ignorance and  misunderstanding about the local terrestrial ecology. It does not, however, restrict itself to the land-based community of creatures as a whole. It extends to the difficulties, challenges, and means of subsistence that  are associated with the landforms of Bohol.",
    start_date=timezone.now(), # not final -> date, image
    end_date=timezone.now(),
    camp=CampEnum.LASANG,
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
)
# Lasang
    #  Projects
 
Project.objects.create(
    title= 'Auditing And Checking On Three Target Municipalities', 
    description= "The purpose of this project is to monitor the growth of the saplings that were planted by the Lasang Committee in Basacdacu, Albur, in September 2020. The purpose of this project is to count the number of saplings that have survived and grown during the year, as well as the different types of saplings that have survived and grown over the year.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.LASANG,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)
Project.objects.create(
    title= 'Creating Signages To Be Placed In Manmade Forest', 
    description= "The purpose of this project, which aims to raise awareness and offer essential information to the public, is to install signages with images and phrases that enlighten visitors about the effects of climate change and encourage them to think twice before throwing their garbage anywhere in the forest.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.LASANG,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)
Project.objects.create(
    title= 'Propagating Saplings', 
    description= "The objective of this project is to propagate and supply seedlings that will be used in tree planting operations. The Executive  Committee of Kabiling Lunhaw has yet to consider the specifics of this action in further detail.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.LASANG,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)

# Baybayon
    #  Events
Event.objects.create(
    title=  ' #Trashtag: Pick A Trash Challenge', 
    description= "This aims to minimize the number of trash in our neighborhood beaches that could end up in the ocean. Through hashtags and documentations, social media will serve as a powerful tool for participants to spread awareness on ocean plastic pollution and encourage other people to take action.",
    start_date=timezone.now(), # not final -> date, image
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
)    
Event.objects.create(
    title=  ' Virtual Run/Walk for the Ocean', 
    description= "This aims to spread awareness, increase public understanding and shape community perceptions on the dangers of ocean plastic pollution. It also aims to generate funds for future projects and activities of Kabiling Lunhaw-Camp Baybayon.",
    start_date=timezone.now(), # not final -> date, image
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
)    
Event.objects.create(
    title=  ' Art out of Trash Contest', 
    description= "This strives to bring awareness to marine debris issues and give litter a new life. This prompts artists to create pieces from items normally thought of as trash.",
    start_date=timezone.now(), # not final -> date, image
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
) 
# Baybayon
    #  Projects
Project.objects.create(
    title= 'Project Pagpahibalo: Kasayuran', 
    description= "This project aims to provide in-depth content on the ocean life of Bohol, as well as the systems that support it, inform the people about the laws, policies and other strategies that would help protect and conserve coastal areas, seas, and oceans, and spread awareness on the importance of environmental conservation, specifically the marine habitats and ecosystems in Bohol.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)    
Project.objects.create(
    title= 'Income Generating Products and Activities', 
    description= "Its goal is to raise funds for future projects of Kabiling Lunhaw-Camp Baybayon that involve the care and preservation of the Oceans and Marine life.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)
Project.objects.create(
    title= 'DYK Social Media Postings', 
    description= "This aims to provide concise and timely facts and information about the ocean and marine life through social media platforms.",
    start_date=timezone.now(), # not final -> date, image   
    end_date=timezone.now(),
    camp=CampEnum.BAYBAYON,
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)
# Suba
    #  Events
Event.objects.create(
    title=  'River Rhapsody: The First Step to River Conservation', 
    description= "It is a webinar tackling the importance, ways and present implementation of conserving and portecting our rivers and watersheds.",
    start_date=timezone.datetime(2021,7,28, tzinfo=timezone.utc), # no time, end date is set the same by hunch   
    end_date=timezone.datetime(2021,7,28, tzinfo=timezone.utc), 
    camp=CampEnum.SUBA, # image not final
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
)    
# Suba
    # Projects
Project.objects.create(
    title= 'Riverside Stories', 
    description= "Its main goal is to interview people residing near rivers, people who have livelihood depending on rivers and those who are tasked to monitor rivers, on their knowledge about the rivers.",
    start_date=timezone.datetime(2021, 9, 1, tzinfo=timezone.utc), # orig date no day, but requires one for datetime
    end_date=timezone.datetime(2021, 9, 1, tzinfo=timezone.utc), 
    camp=CampEnum.SUBA, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)   
Project.objects.create(
    title= "SUBAybay: Kabalo baka's ubang suba sa Bohol, bai?", 
    description= "Its main goal is to visit and showcase through a vlog, to be posted on our social media, the rivers of Bohol which are not yet commonly known.",
    start_date=timezone.datetime(2021, 10, 1, tzinfo=timezone.utc), # orig date no day, but requires one for datetime
    end_date=timezone.datetime(2022, 2, 1, tzinfo=timezone.utc),
    camp=CampEnum.SUBA, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)     
Project.objects.create(
    title= "Membership Disciplinary System", 
    description= "This system will discipline inactive and irresponsible members of the camp, by giving them appropriate consequence for their level of offense.",
    start_date=timezone.datetime(2021, 12, 1, tzinfo=timezone.utc), # orig date no day, but requires one for datetime
    end_date=None, # ongoing, so datetime is None
    camp=CampEnum.SUBA, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)    

Project.objects.create(
    title= "Income Generating Products", 
    description= "We will sell river-themed stickers and t-shirts to both Kabiling Lunhaw and non-Kabiling Lunhaw members, in order to increase our camp's fund.",
    start_date=timezone.datetime(2021,12,1, tzinfo=timezone.utc),   # orig date no day, but requires one for datetime
    end_date=timezone.datetime(2022,3,1, tzinfo=timezone.utc), # ongoing, so datetime is None
    camp=CampEnum.SUBA, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)    
# Zero Waste
    # events
Event.objects.create(
    title= "Tintinan: Moving Towards Zero Waste", 
    description= "A webinar featuring the Zero Waste Island team, it aims to present the Zero Waste Island Tintinan Youth Catalyst Action-its purpose and goal. It will discuss the problem, the intended solution, and what the organization and camp has done so far and what they hope to achieve.",
    start_date=timezone.now(),  # not final -> date, image   
    end_date=timezone.now(), 
    camp=CampEnum.ZEROWASTE, 
    image = Image.objects.create(name=f'event default', image = 'images/content/event.jpg'),
)      
    # projects
Project.objects.create(
    title= "Know More, Waste Less", 
    description= "It intends to raise awareness and shed light to the waste problem by posting facts and information about waste pollution on social media.",
    start_date=timezone.now(),  # not final -> date, image   
    end_date=timezone.now(), 
    camp=CampEnum.ZEROWASTE, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
) 
Project.objects.create(
    title= "Padayon: The Youth for a Zero-Waste Future", 
    description= "This will be a video series featuring not only the members of the camp but also people from and possibly outside the organization as they discuss what it will take to attain a zero-waste future.",
    start_date=timezone.now(),  # not final -> date, image   
    end_date=timezone.now(), 
    camp=CampEnum.ZEROWASTE, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)
Project.objects.create(
    title= "Go Green (Income Generating Products)", 
    description= "Zero-waste products (e.g. towel, bags) with minimalist zero waste theme designs will be sold to Kabiling Lunhaw members and also to the general public.",
    start_date=timezone.now(),  # not final -> date, image   
    end_date=timezone.now(), 
    camp=CampEnum.ZEROWASTE, # image not final
    image = Image.objects.create(name=f'project default', image = 'images/content/project.jpg'),
)