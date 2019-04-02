from django.shortcuts import render
from .models import Team
# Create your views here.

def showTeams(request):
    teams = Team.objects.filter()
    return render(request, 'home.html', {'object_list': teams})