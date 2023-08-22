from django import forms
from Game.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name']  # Add more fields as needed
