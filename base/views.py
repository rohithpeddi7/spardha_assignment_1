from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Games,Team,Team_member
from django.http import HttpResponse
from .forms import TeamForm,MemberForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# games = [
#     {'id':1,'name':'batmintion'},
#     {'id':2,'name':'boxing'},
#     {'id':3,'name':'ttennis'},
# ]
def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')   
    
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'User name or password does not exist')   
    context={'page':page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form=UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during regoistration')
    context={'form':form}
    return render(request,'base/login_register.html',context)

def home(request):
    games=Games.objects.all()
    context={'games':games}
    return render(request, 'base/home.html',context)

def game(request,pk):
    game=Games.objects.get(id=pk)
    teams=Team.objects.filter(game=game)
    context={'game':game,'teams':teams}
    return render(request,'base/games.html',context)

def team(request,pk):
    team = Team.objects.get(id=pk)
    team_members=Team_member.objects.filter(team=team)
    context={'team':team,'team_members':team_members}
    return render(request,'base/teams.html',context)
     
def member_details(request,pk):
    member_details=Team_member.objects.get(id=pk)
    context={'member_details':member_details}
    return render(request,'base/member_details.html',context)

def leader_details(request,pk):
    leader_details=Team.objects.get(id=pk)
    context={'leader_details':leader_details}
    return render(request,'base/leader_details.html',context)
 
@login_required(login_url='login') 
def createTeam(request):
    form = TeamForm()
    
    if request.method == 'POST':
        form = TeamForm(request.POST)
        
        if form.is_valid():
            team = form.save(commit=False)  # Create the team object but don't save yet

            if request.user != team.leader:
                return HttpResponse('Team leader can only be you')

            team.save()
            return redirect('home') 
        
    context = {'form': form}
    return render(request, 'base/add_team_form.html', context)



@login_required(login_url='login') 
def updateTeam(request,pk):
    team=Team.objects.get(id=pk)
    form=TeamForm(instance=team)
    if request.user != team.leader:
        return HttpResponse('Only leader can change configuration')
    
    if request.method=="POST":
        form=TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form':form}
    return render(request,'base/add_team_form.html',context)

@login_required(login_url='login')
def deleteTeam(request,pk):
    team=Team.objects.get(id=pk)
    if request.user != team.leader:
        return HttpResponse('Only leader can change configuration')

    if request.method=='POST':
        team.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':team})

@login_required(login_url='login') 
def addMembers(request,fk):
    team=Team.objects.get(id=fk)
    if request.user != team.leader:
        return HttpResponse('Only leader can change configuration')
    form=MemberForm()
    if request.method == 'POST':
          form=MemberForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')
              
    context={'form':form}
    return render(request,'base/add_member_form.html',context)

@login_required(login_url='login') 
def updateMember(request,pk,fk):
    team=Team.objects.get(id=fk)
    if request.user != team.leader:
        return HttpResponse('Only leader can change configuration')
    member=Team_member.objects.get(id=pk)
    form=MemberForm(instance=member)
    if request.method=="POST":
        form=MemberForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
            return redirect('home')
      
    context={'form':form}
    return render(request,'base/add_member_form.html',context)

@login_required(login_url='login')
def deleteMember(request,pk,fk):
    team=Team_member.objects.get(id=pk)
    teaminfo=Team.objects.get(id=fk)
    if request.user != teaminfo.leader:
        return HttpResponse('Only leader can change configuration')
    if request.method=='POST':
        team.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':team})

# team=Team.objects.get(id=pk) 
# team = get_object_or_404(Team, team_name=team_name)
# if request.user != team.leader:
#     return HttpResponse('Only leader can change configuration')