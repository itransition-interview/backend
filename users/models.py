import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from users.choices import UserRoleType


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=150, blank=True, null=True, default=None)
    username = models.CharField(max_length=150, blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=13, unique=True)
    role = models.CharField(
        max_length=36, choices=UserRoleType.choices,
        default=UserRoleType.USER.value)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"