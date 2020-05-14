import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class BaseUser(PermissionsMixin,
               AbstractBaseUser):
    email = models.EmailField(unique=True)

    name = models.CharField(max_length=255, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    secret_key = models.UUIDField(default=uuid.uuid4, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}'

    def rotate_secret_key(self):
        self.secret_key = uuid.uuid4()
        self.save()

    class Meta:
        ordering = ['email']
