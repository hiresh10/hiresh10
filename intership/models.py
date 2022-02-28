from django.db import models
from django.contrib.auth.models import AbstractUser
from.manager import UserManager




class User(AbstractUser):
    email_tocken = models.CharField(max_length=14)
    email_tocken = models.CharField(max_length=100, null=True, blank=True)
    First_name = models.CharField(max_length=50 , null=True , blank=True)
    Last_name = models.CharField(max_length=50 , null=True, blank=True)
    username = models.CharField(unique=True)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    post = models.CharField(max_length=50)

    object = UserManager
    Required = []
