from django.contrib import admin
from teams.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','team_name', 'game_name', 'game_id')

admin.site.register(Team, TeamAdmin)