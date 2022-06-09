from django.db.models.signals import post_save
from django.dispatch import receiver

from kalunwa.profiles.models import Profile

from .models import User

@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    # Check if it's already created to avoid generating one when there is an 
    # update to the user's info.
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)