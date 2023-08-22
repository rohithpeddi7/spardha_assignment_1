"""
URL configuration for backend_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend_assignment import views

"""
Add your urls here.
There should be one landing page showing the games and teams.
Then make urlpatterns for supporting CRUD operations on these models as you feel.
"""

urlpatterns = [
    path('admin/', admin.site.urls), # Can remove if you wish to, but useful to debug.
    path('thing/',views.thing),
    path('',views.home),
    path('allGames/',views.allGames),
    path('allTeams/',views.allTeams),
    path('allGames/<str:name>',views.particularGame,name="particularGame")
]
