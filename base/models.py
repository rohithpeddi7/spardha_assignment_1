from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here;.
class Games(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)



class Team(models.Model):
    leader=models.ForeignKey(User, on_delete=models.SET_NULL,null =True)
    team_name = models.CharField(max_length=200)
    game=models.ForeignKey(Games, on_delete=models.SET_NULL,null =True)
    updated=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)
    age=models.IntegerField(null=True,blank=True)
    institute_details=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.team_name)
    

class Team_member(models.Model):
    team=models.ForeignKey(Team, on_delete=models.SET_NULL,null =True)
    name=models.CharField(max_length=200)
    age=models.IntegerField(null=True,blank=True)
    institute_details=models.TextField(null=True,blank=True)
        