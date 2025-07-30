from django.db import models

# Create your models here.
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    availability = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.name
