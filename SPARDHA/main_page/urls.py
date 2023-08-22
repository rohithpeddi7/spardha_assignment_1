from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('register/', views.registeruser, name = 'register'),
    # path('addddetails/<str:pk>', views.adddetails, name = 'adddetails'),
    path('', views.maindisplay, name = 'main'),
    path('game/<str:pk>/', views.gamedisplay, name = 'game'),
    path('team/<str:pk>/', views.teamdisplay , name = 'team'),
    path('createteam/', views.createteam, name = 'create-team'),
    path('updateteam/<str:pk>/', views.updateteam, name = 'update-team'),
    path('deleteteam/<str:pk>/', views.deleteteam, name = 'delete-team')
]
