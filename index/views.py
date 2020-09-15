from django.shortcuts import render,redirect
from .models import Match,Player,Team,Contest
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

def team_edit(request,no):
    team = Team.objects.get(id=no)
    match = team.match
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
        'allrounds':allround,
        'players_list':team.players_list.all(),
        'team':team
    }
    return render(request,'teamedit.html',context)

def team_select_submit(request,no):
    if request.method == "POST":
        match = Match.objects.get(match_no=no)
        players = request.POST.getlist('players')
        captain = request.POST["captain"]
        vicecaptain = request.POST["vicecaptain"]
        team_name = request.POST["teamname"]
        if (int(captain) == int(vicecaptain)):
            return redirect('team_select',no=no)
        else:
            cap = Player.objects.get(id=int(captain))
            vicecap = Player.objects.get(id=int(vicecaptain))
            team = Team.objects.create(name=team_name,user=request.user,match=match,captain=cap,vicecaptain=vicecap)
            for i,player in enumerate(players):
                    pla = Player.objects.get(id=int(player))
                    team.players_list.add(player)
            ctx = {
                'players':team,
                'captain':captain,
                'vicecaptain':vicecaptain
            }
            return redirect('contests')
    else:
        return redirect('index')

def team_select_update(request,no):
    if request.method == "POST":
        team = Team.objects.get(id=no)
        match = team.match
        players = request.POST.getlist('players')
        captain = request.POST["captain"]
        vicecaptain = request.POST["vicecaptain"]
        team_name = request.POST["teamname"]
        if (int(captain) == int(vicecaptain)):
            return redirect('team_edit',no=no)
        else:
            cap = Player.objects.get(id=int(captain))
            vicecap = Player.objects.get(id=int(vicecaptain))
            Team.objects.update(name=team_name,user=request.user,match=match,captain=cap,vicecaptain=vicecap)
            team.players_list.clear()
            for i,player in enumerate(players):
                    pla = Player.objects.get(id=int(player))
                    team.players_list.add(player)
            ctx = {
                'players':team,
                'captain':captain,
                'vicecaptain':vicecaptain
            }
            return redirect('teams_list')
    else:
        return redirect('index')

def contests(request):
    contests = Contest.objects.all()
    context = {
        'contests':contests
    }
    return render(request,'contests.html',context)

def teamslist(request):
    user = request.user
    teams_list = Team.objects.filter(user=user)
    context = {
        'teams_list':teams_list
    }
    return render(request,'teamslist.html',context)

def teams_delete(request,no):
    team = Team.objects.get(id=no)
    team.delete()
    return redirect('teams_list')

def contest_join(request,no):
    contest = Contest.objects.get(id=no)
    match = contest.match
    user = request.user
    teams_list = Team.objects.filter(user=user)
    teams_list = Team.objects.filter(match=match)
    count = teams_list.count()
    context = {
        'teams_list':teams_list,
        'contest':contest,
        'count':count
    }
    return render(request,'contest_join.html',context)

def contest_join_submit(request,no):
    if request.method == "POST":
        team = request.POST['radios']
        teamm = Team.objects.get(id=int(team))
        contest = Contest.objects.get(id=no)
        contest.teams.add(teamm)
        contest.save()
        a = "scvajhbsdaseechgvjbngggee"
        a = a+str(teamm.id)+teamm.name
        context = {
            'contest':contest,
            'team':team,
            'rand':a
        }
        return render(request,'esewaform.html',context)
    else:
        return redirect('contest_join',no=no)