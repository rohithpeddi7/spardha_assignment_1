from django.contrib import admin
from games.models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Game, GameAdmin)