import os
from django.db import models
from .models import Demographics, Image
from kalunwa.users.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save
from kalunwa.page_containers.models import PageContainer
from .models import (
    OrgLeader,
    CabinOfficer,
    Commissioner,
    CampLeader
)

# These two auto-delete files from filesystem when they are unneeded:
## Delete file under image field
@receiver(models.signals.post_delete, sender=User)
@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding object is deleted.
    """
    file = instance.image
    if file:
        if os.path.isfile(file.path):
            os.remove(file.path)

@receiver(models.signals.pre_save, sender=User)
@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

###
# -- signals to update single page's update at and their *editors
    # *to add

# post save to update org structure's updated at
@receiver(post_save, sender=OrgLeader, dispatch_uid='org_leader_updates_org_struct_container')
@receiver(post_save, sender=CabinOfficer, dispatch_uid='cabin_officer_updates_org_struct_container')
@receiver(post_save, sender=Commissioner, dispatch_uid='commissioner_updates_org_struct_container')
@receiver(post_save, sender=CampLeader, dispatch_uid='commissioner_updates_org_struct_container')
def update_org_struct_details(sender, instance, *args, **kwargs):
    """
    This updates the organization structure page's editor and updated at, 
    when changes are made to the organization leaders. 
    Called specifically after a successful save. 
    """
    try:
        org_struct_container = PageContainer.objects.get(slug='organization_structure')
        org_struct_container.updated_at = timezone.now()
        # updated with editor as well .. 
        #  org_struct_container.edited_by = instance.edited_by 
        org_struct_container.save()
    except ObjectDoesNotExist: 
        pass 

# post save to update single page demographics container's updated at
@receiver(post_save, sender=Demographics, dispatch_uid='demographics_updates_demographics_page_container')
def update_demographics_details(sender, instance, *args, **kwargs):
    """
    This updates the demographics page's editor and updated at, 
    when changes are made to the organization leaders. 
    Called specifically after a successful save. 
    """
    try:
        demographics_page_container = PageContainer.objects.get(slug='demographics')
        demographics_page_container.updated_at = timezone.now()
        # updated with editor as well .. 
        #  demographics.edited_by = instance.edited_by 
        demographics_page_container.save()
    except ObjectDoesNotExist: 
        pass 