from django import forms
from TeamPlayer.models import TeamPlayer

class TeamPlayerForm(forms.ModelForm):
    class Meta:
        model = TeamPlayer
        fields = ['name', 'age']
