from django.db import models
from manufacturer.models import Manufacturer

# Create your models here.

class CerealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(CerealCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

