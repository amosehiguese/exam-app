from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, is_verified,**kwargs):
        now = timezone.now()
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, is_verified=is_verified, last_login=now, date_joined=now, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, False, False, False)
    
    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, True, True, True, **kwargs)


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name =  models.CharField(max_length=50, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'