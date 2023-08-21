from django.contrib import admin
from players.models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'institute', 'team_name', 'team_id')

admin.site.register(Player, PlayerAdmin)
