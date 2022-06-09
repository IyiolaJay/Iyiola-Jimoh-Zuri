from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)

class Country(models.Model):
    name = models.CharField(max_length=25)