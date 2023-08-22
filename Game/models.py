from django.db import models
from Team.models import Team
# Create your models here.

class Game(models.Model):
    name=models.CharField(max_length=30,unique=True)
    teams = models.ManyToManyField(Team)