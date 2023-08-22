from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class Members(models.Model):
    member = models.OneToOneField(User, on_delete =models.CASCADE, related_name="member")
    age = models.IntegerField()
    institute_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.member.username

class Team(models.Model):
    name = models.CharField(max_length = 50)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    game_name =  models.ForeignKey(Game, on_delete =models.CASCADE, null = True)
    players = models.ManyToManyField(Members, blank = True)

    def __str__(self):
        return self.name
