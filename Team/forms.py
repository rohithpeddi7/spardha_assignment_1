from django import forms
from Team.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'college']
