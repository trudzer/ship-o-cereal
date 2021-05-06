from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cereal.models import Cereal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)