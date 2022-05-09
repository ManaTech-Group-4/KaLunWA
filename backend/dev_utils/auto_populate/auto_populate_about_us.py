"""
- samples for about us
    - dummy data
    
exec(open("dev_utils/auto_populate/auto_populate_about_us.py").read())    
"""
from kalunwa.content.models import (
    CampLeader, 
    Image, 
    CampEnum, 
    CampPage, 
    Demographics, 
    OrgLeader
)

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
        quote = f'quote {_}',
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
    quote = 'quote',
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
    quote = 'quote',
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
    quote = 'quote',
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
    quote = 'quote',
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
    quote = 'quote',
    position = OrgLeader.Positions.AUDITOR,
    
    image=Image.objects.create(
        name = 'auditor',
        image = 'images/content/event.jpg'
    )
)
    
print('populated Org Leaders (5 highest ranks)')
