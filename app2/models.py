from django.db import models

# Create your models here.
class Country(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    