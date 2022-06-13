from kalunwa.content.models import Contributor, Image
"""
actual Contributors
    - some are still not final; see line comments

exec(open("dev_utils/auto_populate/auto_populate_contributors.py").read())
"""

Contributor.objects.create(
    name ="Tagbilaran City Science High School Supreme Student Government",
    category=Contributor.Categories.PARTNER.value,
    image = Image.objects.create(name=f'TCSHS SSG.jpg', image = 'images/content/TCSHS SSG.jpg'),
)


Contributor.objects.create(
    name ="4-H Club Bohol",
    category=Contributor.Categories.PARTNER.value,
    image = Image.objects.create(name=f'4-H Club.jpg', image = 'images/content/4-H Club.jpg'),
)

Contributor.objects.create(
    name ="542nd NROTC- BISU MC",
    category=Contributor.Categories.PARTNER.value,
    image = Image.objects.create(name=f'542nd NROTC- BISU MC.jpg', image = 'images/content/542nd NROTC- BISU MC.jpg'),    
)

Contributor.objects.create(
    name ="Agricultural Training Institute - Central Visayas",
    category=Contributor.Categories.PARTNER.value,
    image = Image.objects.create(name=f'ATI Central Visayas.jpg', image = 'images/content/ATI Central Visayas.jpg'),        
)


Contributor.objects.create(
    name ="Bohol Island State University- Main Campus Supreme Student Government",
    category=Contributor.Categories.PARTNER.value,
    image = Image.objects.create(name=f'BISU MC SSG.jpg', image = 'images/content/BISU MC SSG.jpg'),            
)