from django.contrib import admin
from Team.models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display=("name","college")

admin.site.register(Team,TeamAdmin)