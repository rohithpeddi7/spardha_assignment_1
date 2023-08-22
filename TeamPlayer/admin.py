from django.contrib import admin
from TeamPlayer.models import TeamPlayer
# Register your models here.

class TeamPlayerAdmin(admin.ModelAdmin):
    list_display=("name","age")

admin.site.register(TeamPlayer,TeamPlayerAdmin)