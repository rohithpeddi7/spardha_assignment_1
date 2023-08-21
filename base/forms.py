from django.forms import ModelForm
from .models import Team,Team_member

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields='__all__' 

class MemberForm(ModelForm):
    class Meta:
        model = Team_member
        fields='__all__'         