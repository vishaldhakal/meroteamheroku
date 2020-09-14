from django.shortcuts import render,redirect
from .models import Match,Player,Team
from django.db.models import Q

def index(request):
    top_3_matches = Match.objects.order_by('match_no')[:3]
    context = {
        'top3':top_3_matches
    }
    return render(request,'index.html',context)

def matches(request):
    matchess = Match.objects.order_by('match_no').all()
    context = {
        'matches':matchess
    }
    return render(request,'matches.html',context)

def team_select(request,no):
    match = Match.objects.get(match_no=no)
    criterion1 = Q(player_team=match.teama)
    criterion2 = Q(player_team=match.teamb)
    q = Player.objects.filter(criterion1 | criterion2)
    batsman = q.filter(position="Batsman")
    bowler = q.filter(position="Bowler")
    wicket = q.filter(position="Wicket Keeper")
    allround = q.filter(position="All Rounder")
   
    context = {
        'match':match,
        'batsmans':batsman,
        'bowlers':bowler,
        'wickets':wicket,
        'allrounds':allround
    }
    return render(request,'team_select.html',context)

def team_select_submit(request,no):
    if request.method == "POST":
        players = request.POST.getlist('players')
        captain = request.POST["captain"]
        vicecaptain = request.POST["vicecaptain"]
        if (int(captain) == int(vicecaptain)):
            return redirect('team_select',no=no)
        else:
            team = Team.objects.create(name="sds",user=request.user)
            for i,player in enumerate(players):
                    pla = Player.objects.get(id=int(player))
                    team.players_list.add(player)
            ctx = {
                'players':team,
                'captain':captain,
                'vicecaptain':vicecaptain
            }
            return render(request,'test.html',ctx)
    else:
        return redirect('index')