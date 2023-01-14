from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

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
        return self._create_user(email, password, is_staff=False, is_superuser=False, is_verified=False, **kwargs)
    
    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, is_staff=True, is_superuser=True, is_verified=True, **kwargs)


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(_('first name'),max_length=50, blank=True)
    last_name =  models.CharField(_('last name'),max_length=50, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_verified = models.BooleanField(_('verified'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table='users'