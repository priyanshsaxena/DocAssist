from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Disease(models.Model):
	disease_name = models.CharField(max_length=100)
	disease_symptoms = models.CharField(max_length=5000)
	disease_probability = models.FloatField(default=0.0)

class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_age = models.PositiveIntegerField()
    patient_disease = models.CharField(max_length=100)

class Material(models.Model):
	disease = models.CharField(max_length=300,default="")
	material_url = models.URLField(max_length=300,default="http://google.com")
	material_image_url = models.URLField(max_length=300,default="http://google.com")
	material_rating = models.PositiveIntegerField()