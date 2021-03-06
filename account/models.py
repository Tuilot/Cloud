from datetime import date

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class Account(AbstractUser, PermissionsMixin):
    id = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30, default="")
    school = models.CharField(max_length=150, default="")
    profession = models.CharField(max_length=1000, default="")
    register_data = models.DateField(default=date.today)
    is_superuser = models.BooleanField(default=False)
    real_name = models.CharField(max_length=1000, default="")
    sex = models.CharField(max_length=1000, default="")
    avatar = models.FileField(default='avatar/default_avatar.png', upload_to='avatar/')
    motto = models.CharField(max_length=1000, default="")
    fans_count = models.IntegerField(default=0)

    class Meta:
        permissions = [
            ("manager", "Can manager the website"),
        ]


class Follow(models.Model):
    fans = models.CharField(max_length=20)
    uploader = models.CharField(max_length=20)
    follow_time = models.DateTimeField(auto_now_add=True)
