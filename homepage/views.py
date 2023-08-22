from django.shortcuts import render
from .models import games,players,teams
from django.contrib.auth.models import User
# Create your viewfrs here.
def home(request):
    x = games.objects.all().values()
    context={
        'x':x,
    }
    return render(request,"home.html",context)

def team(request,game_name):
    y = game_name
    z =set()
    p= games.objects.values_list('game_name')
    if (y,) in p:
        x = teams.objects.filter(game_name=y).values_list("Team_name")
        for a in x:
            a=list(a)
            for b in a:
                z.add(b)
        context={
            'x':x,
            'y':y,
            'z':z
        }
        return render(request,'teams.html',context)
    else :
        return render(request,'404.html')

def player(request,game_name,Team_name):
    y = Team_name
    z = game_name
    temp = teams.objects.all().values_list('game_name','Team_name')
    if (z,y,) in temp:
        x = teams.objects.filter(game_name=z,Team_name=y).values_list('player_name')
        temp =[]
        for a in x:
            a=list(a)
            a = str(a[0])
            temp.append(a)
        context = {
            'x': x,
            'y': y,
            'temp':temp,
            'z':z,
        }
        return render(request,'players.html',context)
    else :
        return render(request, '404.html')


def playerpersonal(request,game_name,Team_name,name):
    y = game_name
    z = Team_name
    t = name
    x = players.objects.filter(name=t).values()[0]
    context = {
        'x': x,
        'y': y,
        'z':z,
        't':t,
    }
    return render(request, 'playersPersonals.html', context)

def newplayer(request,game_name):
    game1 = game_name
    name1 = " "
    if request.method == 'POST':
        name1 = request.POST['name']
        game1 = request.POST['game']
        team1 = request.POST['team']
        age1 = request.POST['age']
        state1 = request.POST['state']
        institute1 = request.POST['institute']
        context = {
            'name1': name1,
            'game1': game1,
            'team1': team1,
        }
        temp = teams.objects.filter(game_name=game1).values_list('player_name')
        if (name1,) in temp:
            return render(request,'error.html',context)
        temp = teams.objects.filter(game_name=game1).values_list('player_name')
        x = teams(game_name=game1, Team_name=team1, player_name=name1)
        x.save()
        x = players(name=name1, age=age1, state=state1, institute=institute1)
        x.save()
        return render(request,'complete.html',context)
    else :
        context={
            'game1':game1,
            'name1':name1,
        }
        return render(request,'registration.html',context)

def update(request,game_name,Team_name,player_name):
    a = game_name
    b= Team_name
    c= player_name
    if request.method == 'POST':
        name1 = request.POST['name']
        game1 = request.POST['game']
        team1 = request.POST['team']
        age1 = request.POST['age']
        state1 = request.POST['state']
        institute1 = request.POST['institute']
        context = {
            'name1': name1,
            'game1': game1,
            'team1': team1,
        }
        temp = teams.objects.filter(game_name=game1).values_list('player_name')
        if (name1,) in temp:
            return render(request,'error.html',context)
        x = teams.objects.filter(player_name=c,game_name=a)
        x.delete()
        x = teams(game_name=game1, Team_name=team1, player_name=name1)
        x.save()
        x= players.objects.filter(name=c)
        x.delete()
        x = players(name=name1, age=age1, state=state1, institute=institute1)
        x.save()
        return render(request,'updated.html',context)
    else :
        context={
            'a':a,
            'b':b,
            'c':c,
        }
        return render(request,'update.html',context)



