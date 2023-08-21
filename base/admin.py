from django.contrib import admin

# Register your models here.
from .models import Games,Team,Team_member

admin.site.register(Games)
admin.site.register(Team)
admin.site.register(Team_member)
