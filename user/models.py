from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cereal.models import Cereal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    profile_image = models.CharField(max_length=9999)

    def __str__(self):
        return self.first_name