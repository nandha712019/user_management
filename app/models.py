from datetime import date
from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.TextField(default='00/00, address**')
    salary = models.IntegerField()
    date_joined = models.DateField(default=date.today())
