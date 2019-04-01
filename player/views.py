from django.shortcuts import render
from .models import Player
from team.models import Team
from .forms import searchPlayer
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.

def showPlayers(request, pk):
    players = Player.objects.filter(team__pk=pk)
    team = Team.objects.filter(pk=pk)
    return render(request, 'team.html', {'object_list': players, 'team': team})

def playerDetail(request, pk):
    player = Player.objects.filter(pk=pk)
    return render(request, 'player.html', {'object_list': player})

def playerSearch(request, pk):
    form = searchPlayer()
    player = Player.objects.filter(pk=pk)
    if request.method == "POST":
        form = searchPlayer(request.POST)
        if form.is_valid():
                
                l = ['value', 'pace', 'shooting', 'passing', 'dribbling', 'defence', 'physical']
                k = []

                for i in l:
                        if form.cleaned_data[i] is None:
                                k.append(100000000)
                        else:
                                k.append((form.cleaned_data[i]))
                
                p = Player.objects.filter(position=player[0].position).filter(value__lte=(float(player[0].value)+float(k[0]))).filter(value__gte=(float(player[0].value)-float(k[0]))).filter(pace__lte=((player[0].pace)+int(k[1]))).filter(pace__gte=((player[0].pace)-int(k[1]))).filter(shooting__lte=(player[0].shooting+k[2])).filter(shooting__gte=(player[0].shooting-k[2])).filter(passing__lte=(player[0].passing+k[3])).filter(passing__gte=(player[0].passing-k[3])).filter(dribbling__lte=(player[0].dribbling+k[4])).filter(dribbling__gte=(player[0].dribbling-k[4])).filter(defence__lte=(player[0].defence+k[5])).filter(defence__gte=(player[0].defence-k[5])).filter(physical__lte=(player[0].physical+k[6])).filter(physical__gte=(player[0].physical-k[6]))

                shortlist = []

                for l in p:
                        if l.team.team_name == player[0].team.team_name:
                                pass
                        else:
                                shortlist.append(l)



                return render(request, 'results.html', {'object_list': player, 'shortlist':shortlist})
    return render(request, 'form.html', {'object_list': player, 'form':form})

