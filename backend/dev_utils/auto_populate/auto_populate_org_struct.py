'''
actual execomm, camp leaders then dummy for commissioners and cabin officers

exec(open("dev_utils/auto_populate/auto_populate_org_struct.py").read())
'''

from kalunwa.content.models import (
    CampLeader, 
    Image, 
    CampEnum, 
    OrgLeader,
    Commissioner,
    CabinOfficer
)


#------------ Org Leaders (ExeComm, Directors)

# President
OrgLeader.objects.create(
    first_name = 'Jairus',
    last_name = 'Chiu',
    quote = 'quote',
    position = OrgLeader.Positions.PRESIDENT,

    image=Image.objects.create(
        name = f'pres',
        image = 'images/content/leaders/President.jpg'
    )
)

# Vice President
OrgLeader.objects.create(
    first_name = 'Claire Marie',
    last_name = 'Hernando',
    quote = 'quote',
    position = OrgLeader.Positions.VICE_PRESIDENT,
    
    image=Image.objects.create(
        name = 'vpres',
        image = 'images/content/leaders/VicePresident.jpg'
    )
)

# Secretary
OrgLeader.objects.create(
    first_name = 'Chen',
    last_name = 'Lomosbog',
    quote = 'quote',
    position = OrgLeader.Positions.SECRETARY,
    
    image=Image.objects.create(
        name = 'secretary',
        image = 'images/content/leaders/Secretary.jpg'
    )
)

# Treasurer
OrgLeader.objects.create(
    first_name = 'Cherry Joyce',
    last_name = 'Bongcaras',
    quote = 'quote',
    position = OrgLeader.Positions.TREASURER,
    
    image=Image.objects.create(
        name = 'treasurer',
        image = 'images/content/leaders/Treasurer.jpg'
    )
)

# Auditor
OrgLeader.objects.create(
    first_name = 'Julianne Pearl',
    last_name = 'Ayco',
    quote = 'quote',
    position = OrgLeader.Positions.AUDITOR,
    
    image=Image.objects.create(
        name = 'auditor',
        image = 'images/content/leaders/Auditor.jpg'
    )
)


# PIO
OrgLeader.objects.create(
    first_name = 'Alyssa Danielle',
    last_name = 'Pangan',
    quote = 'quote',
    position = OrgLeader.Positions.PIO,
    
    image=Image.objects.create(
        name = 'pio',
        image = 'images/content/leaders/PIO.jpg'
    )
)

# Overseer
OrgLeader.objects.create(
    first_name = 'Nina Althea',
    last_name = 'Gucor',
    quote = 'quote',
    position = OrgLeader.Positions.OVERSEER,
    
    image=Image.objects.create(
        name = 'overseer',
        image = 'images/content/leaders/Overseer.jpg'
    )
)

# Directors
OrgLeader.objects.create(
    first_name = 'Michael Ethan',
    last_name = 'Chiu',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir1',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'John Andrew',
    last_name = 'Aton',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir2',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Juvel James',
    last_name = 'Dumayaca',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir3',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Dignity',
    last_name = 'Lagunay',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir4',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Jairus Zim',
    last_name = 'Pasagad',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir5',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Rami Ezra',
    last_name = 'Lanoy',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir6',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Kayla Maria',
    last_name = 'Simpao',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir7',
        image = 'images/content/event.jpg'
    )
)

OrgLeader.objects.create(
    first_name = 'Rene Emmanuel',
    last_name = 'Villaber',
    quote = 'quote',
    position = OrgLeader.Positions.DIRECTOR,
    
    image=Image.objects.create(
        name = 'dir8',
        image = 'images/content/event.jpg'
    )
)


print('populated org leaders')


#------------ Commissioner (dummy no info from KL yet)

for _ in range(2):
    dummy_image = Image.objects.create(
        name = f'commissioner {_}',
        image = 'images/content/event.jpg'
    )   

    Commissioner.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        quote = f'quote {_}',
        image=dummy_image,
        category = Commissioner.Categories.values[_],
        position = Commissioner.Positions.values[_]
    )
   
print('populated commissioners')



##------------ Camp Leaders

# Baybayon : Camp Leader
CampLeader.objects.create(
    first_name = 'Marielle Eliza',
    last_name = 'Mascariñas',
    quote = 'quote',
    camp = CampEnum.BAYBAYON,
    position = CampLeader.Positions.LEADER,

    image=Image.objects.create(
        name = f'BaybayonCL',
        image = 'images/content/leaders/Baybayon_CL.JPG'
    )
)

# Baybayon : Assistant Leader
CampLeader.objects.create(
    first_name = 'Tyra Jae',
    last_name = 'Galan',
    quote = 'quote',
    camp = CampEnum.BAYBAYON,
    position = CampLeader.Positions.ASSISTANT_LEADER,

    image=Image.objects.create(
        name = f'BaybayonACL',
        image = 'images/content/leaders/Baybayon_ACL.jpg'
    )
)

# Lasang : Camp Leader
CampLeader.objects.create(
    first_name = 'Spica Mae',
    last_name = 'Samante',
    quote = 'quote',
    camp = CampEnum.LASANG,
    position = CampLeader.Positions.LEADER,

    image=Image.objects.create(
        name = f'LasangCL',
        image = 'images/content/leaders/Lasang_CL.JPG'
    )
)

# Lasang : Assistant Leader
CampLeader.objects.create(
    first_name = 'Jyra Maria',
    last_name = 'Usaraga',
    quote = 'quote',
    camp = CampEnum.LASANG,
    position = CampLeader.Positions.ASSISTANT_LEADER,

    image=Image.objects.create(
        name = f'LasangACL',
        image = 'images/content/leaders/Lasang_ACL.jpg'
    )
)

# Suba : Camp Leader
CampLeader.objects.create(
    first_name = 'Noelyn Faith',
    last_name = 'Lopos',
    quote = 'quote',
    camp = CampEnum.SUBA,
    position = CampLeader.Positions.LEADER,

    image=Image.objects.create(
        name = f'SubaCL',
        image = 'images/content/leaders/Suba_CL.jpg'
    )
)

# Suba : Assistant Leader
CampLeader.objects.create(
    first_name = 'Gervie Faye',
    last_name = 'Olarita',
    quote = 'quote',
    camp = CampEnum.SUBA,
    position = CampLeader.Positions.ASSISTANT_LEADER,

    image=Image.objects.create(
        name = f'SubaACL',
        image = 'images/content/leaders/Suba_ACL.jpg'
    )
)

# Zero Waste : Camp Leader
CampLeader.objects.create(
    first_name = 'Emirozz Czarlene',
    last_name = 'Labaria',
    quote = 'quote',
    camp = CampEnum.ZEROWASTE,
    position = CampLeader.Positions.LEADER,

    image=Image.objects.create(
        name = f'ZeroWasteCL',
        image = 'images/content/leaders/ZeroWaste_CL.JPG'
    )
)

# Zero Waste : Camp Leader
CampLeader.objects.create(
    first_name = 'Princess',
    last_name = 'Te',
    quote = 'quote',
    camp = CampEnum.ZEROWASTE,
    position = CampLeader.Positions.ASSISTANT_LEADER,

    image=Image.objects.create(
        name = f'ZeroWasteACL',
        image = 'images/content/leaders/ZeroWaste_ACL.JPG'
    )
)

print('populated camp leaders')


##------------ Cabin Officers (dummy no info from KL)

#Baybayon
for _ in range(4):
    dummy_image = Image.objects.create(
        name = f'Baybayon cabinOfficer {_}',
        image = 'images/content/event.jpg'
    )   

    CabinOfficer.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        quote = f'quote {_}',
        image=dummy_image,
        category = CabinOfficer.Categories.values[_],
        camp = CampEnum.BAYBAYON,
        position = CabinOfficer.Positions.values[_]
    )

#Lasang
for _ in range(4):
    dummy_image = Image.objects.create(
        name = f'Lasang cabinOfficer {_}',
        image = 'images/content/event.jpg'
    )   

    CabinOfficer.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        quote = f'quote {_}',
        image=dummy_image,
        category = CabinOfficer.Categories.values[_],
        camp = CampEnum.LASANG,
        position = CabinOfficer.Positions.values[_]
    )

#Suba
for _ in range(4):
    dummy_image = Image.objects.create(
        name = f'Suba cabinOfficer {_}',
        image = 'images/content/event.jpg'
    )   

    CabinOfficer.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        quote = f'quote {_}',
        image=dummy_image,
        category = CabinOfficer.Categories.values[_],
        camp = CampEnum.SUBA,
        position = CabinOfficer.Positions.values[_]
    )

#Zero Waste
for _ in range(4):
    dummy_image = Image.objects.create(
        name = f'ZeroWaste cabinOfficer {_}',
        image = 'images/content/event.jpg'
    )   

    CabinOfficer.objects.create(
        first_name = f'firstname {_}',
        last_name = f'lastname {_}',
        quote = f'quote {_}',
        image=dummy_image,
        category = CabinOfficer.Categories.values[_],
        camp = CampEnum.ZEROWASTE,
        position = CabinOfficer.Positions.values[_]
    )

print('populated cabin officers')