from django.contrib import admin

# Register your models here.

from .models import Game,Members,Team

admin.site.register(Game)
admin.site.register(Members)
admin.site.register(Team)