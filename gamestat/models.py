
from django.db import models
from django.contrib.auth.models import User
from .RECORDS import records




class Genre(models.Model):
    genre= models.CharField(blank= True, choices=  records.genre, max_length=12)

class Platform(models.Model):
    platfrom= models.CharField(blank= True, choices= records.platform, max_length=12)


class Statistic(models.Model):
    name= models.ForeignKey(User, on_delete= models.CASCADE)
    genre= models.ForeignKey(Genre, on_delete= models.CASCADE)
    platform= models.ForeignKey(Platform, on_delete=models.CASCADE)







# Create your models here.
