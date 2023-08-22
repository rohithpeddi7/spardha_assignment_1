from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Game ,Team ,Members
from .forms import TeamForm


def loginpage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request , username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {
        'page': page
    }
    return render(request, 'login_register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('main')

def registeruser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    context = {
        'page' : page,
        'form' : form
    }
    return render(request, 'login_register.html', context)


def maindisplay(request):
    Games = Game.objects.all().values()
    context = {
        'Games' : Games,
    }
    return render(request, 'mainpage.html', context)

def gamedisplay(request, pk):
    game = Game.objects.get(id = pk )
    teams = Team.objects.filter(game_name = game)
    context = {
        'game' : game,
        'teams' : teams
    }
    return render(request, 'gamepage.html', context)
    
def teamdisplay(request, pk):
    team = Team.objects.get(id = pk)
    context = {
        'team' : team
    }
    return render(request, 'teampage.html', context)

@login_required(login_url = 'login')
def createteam(request):
    form = TeamForm()
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {
        'form' : form
    }
    return render(request, 'team_form.html', context)

@login_required(login_url = 'login')
def updateteam(request, pk):
    team = Team.objects.get(id = pk)
    form = TeamForm(instance = team)

    if request.user != team.leader:
        return HttpResponse('Only leader can change the team!!')
    
    if request.method == "POST":
        form = TeamForm(request.POST, instance = team)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {
        'form' : form
    }
    return render(request, 'team_form.html', context)

@login_required(login_url = 'login')
def deleteteam(request, pk):
    team = Team.objects.get(id = pk)

    if request.user != team.leader:
        return HttpResponse('Only leader can delete the team!!')
    
    if request.method == "POST":
        team.delete()
        return redirect('main')
    context = {
        'team' : team
    }
    return render(request, 'deleteteam.html', context)