from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('',views.home,name='home'),
    path('game/<str:pk>',views.game,name='game'),
    path('team/<str:pk>/',views.team,name='team'),
    path('member_details/<str:pk>/',views.member_details,name='member_details'),
    path('leader_details/<str:pk>/',views.leader_details,name='leader_details'),
    path('create-team/',views.createTeam,name="create-team"),
    path('update-team/<str:pk>/',views.updateTeam,name="update-team"),
    path('add-members/<str:fk>/',views.addMembers,name='add-member'),
    path('update-members/<str:pk>/<str:fk>/',views.updateMember,name='update-member'),
    path('delete-team/<str:pk>/',views.deleteTeam,name='delete-team'),
    path('delete-member/<str:pk>/<str:fk>/',views.deleteMember,name='delete-member'),

]