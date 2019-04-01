from django.shortcuts import render
from .models import Team
# Create your views here.

def showTeams(request):
    teams = Team.objects.filter()
    

    # x = "Arsenal,Bournemouth,Brighton & Hove Albion,Burnley,Cardiff City,Chelsea,Crystal Palace,Everton,Fulham,Huddersfield Town,Leicester City,Liverpool,Manchester City,Manchester United,Newcastle United,Southampton,Tottenham Hotspur,Watford,West Ham United,Wolverhampton Wanderers"
    # x = x.split(",")

    # for i in x:
    #     p = Team.objects.create(team_name=i)
    #     p.save()
    


    return render(request, 'home.html', {'object_list': teams})