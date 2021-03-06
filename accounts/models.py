from datetime import timedelta
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils import timezone

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            username = email,
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, email,full_name=None, password=None):
        user = self.create_user(
                username=username,
                email=email,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, username, email, full_name=None, password=None):
        user = self.create_user(
                username=username,
                email=email,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class Client(AbstractBaseUser):
    username   = models.CharField(max_length=255, blank=True, null=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    is_active   = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    email = models.EmailField(verbose_name='email', max_length=60, unique=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    # @property
    # def is_active(self):
    #     return self.active



class Driver(AbstractBaseUser):
    username   = models.CharField(max_length=255, blank=True, null=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    is_active   = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    email = models.EmailField(verbose_name='email', max_length=60, unique=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    # USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    # @property
    # def is_active(self):
    #     return self.active