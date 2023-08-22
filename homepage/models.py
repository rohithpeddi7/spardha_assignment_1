from django.db import models
# Create your models here.

class games(models.Model):
    game_name = models.CharField(max_length=50)

class teams(models.Model):
    game_name = models.CharField(max_length=50)
    Team_name = models.CharField(max_length=50)
    player_name = models.CharField(max_length=50)

class players(models.Model):
    name = models.CharField(max_length=50,unique=True)
    age = models.IntegerField()
    state = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)


