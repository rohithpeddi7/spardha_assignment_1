from django.contrib import admin
from Game.models import Game
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Game,GameAdmin)