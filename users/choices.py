from django.db import models


class UserRoleType(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'