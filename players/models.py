from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
    ])
    institute = models.CharField(max_length=60)
    team_id = models.IntegerField(default=0)
    team_name = models.CharField(max_length=60, default="null")
