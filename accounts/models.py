from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'), blank=True, related_name='custom_user_set')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
