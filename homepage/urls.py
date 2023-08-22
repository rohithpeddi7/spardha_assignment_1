from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('<str:game_name>/',views.team,name="teams"),
    path('<str:game_name>/register/',views.newplayer,name="newplayer"),
    path('<str:game_name>/<str:Team_name>/',views.player,name="players"),
   path("<str:game_name>/<str:Team_name>/<str:name>/",views.playerpersonal,name="playerpersonal"),
   path("<str:game_name>/<str:Team_name>/<str:player_name>/update",views.update,name="update"),


]
