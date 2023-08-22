from django.contrib import admin
from Users.models import Users
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display=("name","age")

admin.site.register(Users,UsersAdmin)