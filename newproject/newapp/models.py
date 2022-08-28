from django.db import models
class Registration(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    technology = models.CharField(max_length=50)
    candidatetype = models.CharField(max_length=50)
    higereducation = models.CharField(max_length=50)
    Passingyear = models.CharField(max_length=50)
# Create your models here.
