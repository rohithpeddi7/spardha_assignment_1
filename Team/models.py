from django.db import models
from TeamPlayer.models import TeamPlayer
# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=30,unique=True)
    college=models.CharField(default="faltu sa koi",max_length=50)
    players=models.ManyToManyField(TeamPlayer)
