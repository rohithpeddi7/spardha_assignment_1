from django.db import models

class Team(models.Model):
    game_id = models.IntegerField()
    team_name = models.CharField(max_length=30)
    game_name = models.CharField(max_length=30,default="null")
