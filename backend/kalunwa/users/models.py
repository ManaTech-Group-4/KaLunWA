from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# user profile
    # first_name = models.CharField(max_length=150, blank=True) -> profile
    # last_name = models.CharField(max_length=150, blank=True)    
    # image = 
    # created 

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields): # superadmin?

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address') # change to drf errors

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password) # hashes password
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin): # permission for django facilities
    email = models.EmailField(unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    # a username field is default for login, so we override it to use the 
    # email instead
    USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []    

    def __str__(self):
        return self.user_name

    def get_role(self):
        pass