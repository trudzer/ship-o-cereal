from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateTimeField()
    logo = models.CharField(max_length=9999, blank=True)

    def __str__(self):
        return self.name