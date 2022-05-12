"""
- samples for about us
    - dummy data
    
exec(open("dev_utils/auto_populate/auto_populate_about_us.py").read())    
"""
from kalunwa.content.models import (
    Image, 
    CampEnum, 
    CampPage, 
    Demographics, 
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
