from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.name