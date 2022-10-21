from django.contrib.auth.models import AbstractUser
# from django.db import models


class Admin(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Admin'

