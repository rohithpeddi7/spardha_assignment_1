## Add the necessary views for each urlpattern here.
from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from Game.models import Game
from Team.models import Team

from Game.forms import GameForm
from Team.forms import TeamForm
from TeamPlayer.forms import TeamPlayerForm

#todo: add teams to games, add players to teams, show players pertaining to team
#todo: delete games, teams, players

def thing(request):
    return HttpResponse("hiiii")

def home(request):
    return render(request,"index.html")

def allGames(request):
    # if request.method == 'GET':
    form=GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Attempt to save the form data
                
            except IntegrityError:
                form.add_error('name', 'A game with this name already exists.')
        else:
            form.add_error(None, 'The form is invalid.')
         
    gameData=Game.objects.all()
    return render(request,"allGames.html",{'gameData':gameData,'form':form})

def particularGame(request,name):
    gameData=get_object_or_404(Game,name=name)
    if request.method == 'GET':
        return render(request,"particularGame.html",{'gameData':gameData,'form':TeamForm()})
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            try:
                newteam=form.save()  # Attempt to save the form data
                gameData.teams.add(newteam)
                return redirect('particularGame',name=name)
            except IntegrityError:
                form.add_error('name', 'A team with this name already exists.')
        else:
            form.add_error(None, 'The form is invalid.')
        gameData=get_object_or_404(Game,name=name)
        return render(request,"particularGame.html",{'gameData':gameData,'form':form})

def allTeams(request):
    if request.method == 'GET':
        teamData=Team.objects.all()
        return render(request,"allTeams.html",{'teamData':teamData})
    
def particularTeam(request,name):
    teamData=get_object_or_404(Team,name=name)
    print("fdsfsaa",teamData.players.all())
    if request.method == 'GET':
        return render(request,"particularTeam.html",{'teamData':teamData,'form':TeamPlayerForm()})
    if request.method == 'POST':
        form = TeamPlayerForm(request.POST)
        if form.is_valid():
            try:
                newplayer=form.save()  # Attempt to save the form data
                teamData.players.add(newplayer)
                return redirect('particularTeam',name=name)
            except IntegrityError:
                form.add_error('name', 'A player with this name already exists.')
        else:
            form.add_error(None, 'The form is invalid.')
        teamData=get_object_or_404(Team,name=name)
        return render(request,"particularTeam.html",{'teamData':teamData,'form':form})
        