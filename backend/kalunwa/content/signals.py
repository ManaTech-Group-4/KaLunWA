import os

from django.db import models
from django.dispatch import receiver
from .models import Image
from kalunwa.users.models import User

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