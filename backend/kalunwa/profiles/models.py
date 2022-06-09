from django.db import models
from kalunwa.core.models import TimestampedModel
# Create your models here.

class Profile(TimestampedModel):
    user = models.OneToOneField(
        'users.User', on_delete=models.CASCADE
    )
    # here we are referencing directly to the model that uses an image,
    # because unlike images that are related to content, profile images are
    # not assets that should be shared around in some endpoint. 
    image = models.ImageField(upload_to='images/profile-photos/')  

    def __str__(self):
        return f'Profile: {self.user.get_fullname()}'

    def get_role(self):
        if self.user.is_superuser:
            return 'Super Admin'            
        return 'Admin'