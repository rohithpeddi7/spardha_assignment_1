## Add the necessary views for each urlpattern here.
from django.shortcuts import render
from games.models import Game
from teams.models import Team
from players.models import Player
from django.contrib import messages
from django.shortcuts import redirect

def home(req):
    try:
        games = Game.objects.all().order_by('name')
        teams = Team.objects.all().order_by('team_name', 'game_name')
        players = Player.objects.all().order_by('name', 'institute')
        data = {
            'games': games,
            'teams': teams,
            'players': players
        }
        return render(req, 'Home.html',data)
    except Exception as e:
        print(e)
    

def registerTeam(req):
    try:
        games = Game.objects.all().order_by('name')
        data = {
            'games': games,
            'success': True
        }
        if req.method == "POST":
            game = req.POST.get('game_id').split('-')
            game_id = game[0]
            game_name = game[1]
            team_name = req.POST.get('team_name')
            team_exists = Team.objects.filter(team_name=team_name).exists()
            if team_exists:
                for team in Team.objects.filter(team_name=team_name):
                    if int(team.game_id) == int(game_id):
                        messages.error(req, "Team already exists in the chosen game")
                        print("Team already exists")
                        data['success'] = False
                        return render(req, 'registerTeam.html', data)
                dataToSave = Team(game_id=game_id, team_name=team_name, game_name=game_name);
                dataToSave.full_clean()
                dataToSave.save()
            else:
                dataToSave = Team(game_id=game_id, team_name=team_name, game_name=game_name);
                dataToSave.full_clean()
                dataToSave.save()
            messages.success(req, "Registered Team successfully")
        return render(req, 'registerTeam.html', data)
    except Exception as e:
        print(e)

def addPlayers(req):
    try:
        teams = Team.objects.all().order_by('team_name', 'game_name')
        data = {
            'teams': teams,
        }
        if req.method == "POST":
            team = req.POST.get('team').split('-')
            team_id = team[0]
            team_name = f"{team[1]} ({team[2]})"
            game_name = team[2]
            player_name = req.POST.get('player_name')
            age = req.POST.get('age')
            institute = req.POST.get('institute')
            player_obj = Player(name=player_name,age=age,institute=institute, team_id=team_id, team_name=team_name)
            player_obj.full_clean()
            player_obj.save()
        return render(req, 'addPlayers.html', data)
    except Exception as e:
        print(e)



