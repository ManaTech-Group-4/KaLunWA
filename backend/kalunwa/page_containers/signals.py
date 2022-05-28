
from django.db import IntegrityError
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.forms import ValidationError
from .models import PageContainer
from kalunwa.core.utils import unique_slugify

@receiver(pre_save, sender=PageContainer, dispatch_uid='create_page_container_slug')
def pre_save(sender, instance, *args, **kwargs):
   instance.slug = unique_slugify(instance, instance.name)



