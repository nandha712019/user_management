from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    address = models.TextField(default='00/00, address**')
    salary = models.IntegerField(default=0, null=False, blank=False)
    date_joined = models.DateField(default=date.today(), null=False, blank=False)
