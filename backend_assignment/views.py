## Add the necessary views for each urlpattern here.
from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from Game.models import Game
from Team.models import Team
from Game.forms import GameForm

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
    if request.method == 'GET':
        gameData=get_object_or_404(Game,name=name)
        return render(request,"particularGame.html",{'gameData':gameData})

def allTeams(request):
    if request.method == 'GET':
        teamData=Team.objects.all()
        return render(request,"allTeams.html",{'teamData':teamData})