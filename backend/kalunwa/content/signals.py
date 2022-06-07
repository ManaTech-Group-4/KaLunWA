from django.dispatch import receiver
from django.db.models.signals import pre_save
from kalunwa.content.models import (
    CampPage
)
from kalunwa.core.utils import unique_slugify

@receiver(pre_save, sender=CampPage, dispatch_uid='create_camp_slug')
def pre_save(sender, instance, *args, **kwargs):
    print(instance.get_name())
    instance.slug = unique_slugify(instance, instance.get_name())