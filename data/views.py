from django.shortcuts import render, redirect  
from data.forms import GameForm 
from data.models import Games  
# Create your views here. 

 
def games(request):  
    if request.method == "POST":  
        form = GameForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = GameForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    game = Games.objects.all()  
    return render(request,"show.html",{'Games':game})  

def edit(request, id):  
    game = Games.objects.get(id=id)  
    return render(request,'edit.html', {'Games':game})  

def update(request, id):  
    game = Games.objects.get(id=id)  
    form = GameForm(request.POST, instance = game)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'Games': game})  

def delete(request, id):  
    game = Games.objects.get(id=id)  
    game.delete()  
    return redirect("/show")  