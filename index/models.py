from django.db import models
from django.contrib.auth.models import User


class Franchise(models.Model):
    name = models.CharField(max_length=100)
    net_run_rate = models.FloatField(default=0.0)
    match_played = models.IntegerField(default=0)
    match_won = models.IntegerField(default=0)
    logo = models.FileField()

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = [
    ('Batsman', 'Batsman'),
    ('Bowler', 'Bowler'),
    ('Wicket Keeper', 'Wicket Keeper'),
    ('All Rounder', 'All Rounder'),
    ]
    COUNTRY_CHOICES = [
    ('India', 'India'),
    ('Australlia', 'Australlia'),
    ('England', 'England'),
    ('New Zealand', 'New Zealand'),
    ('West Indies', 'West Indies'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    image = models.FileField(default='virat.png')
    player_team = models.ForeignKey(Franchise,on_delete=models.CASCADE)
    credits = models.FloatField(default=0)
    points = models.FloatField(default=0)
    position = models.CharField(
        max_length=200,
        choices=POSITION_CHOICES,
        default='Batsman',
    )
    country = models.CharField(
        max_length=200,
        choices=COUNTRY_CHOICES,
        default='India',
    )

    def __str__(self):
        return self.name

class Match(models.Model):
    match_no = models.IntegerField()
    teama = models.ForeignKey(Franchise,on_delete=models.CASCADE,related_name="teama")
    teamb = models.ForeignKey(Franchise,on_delete=models.CASCADE,related_name="teamb")
    match_date = models.DateTimeField(auto_now_add=False,auto_now=False)
    
    def __str__(self):
        return self.teama.name+self.teamb.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    players_list = models.ManyToManyField(Player,blank=True)
    captain = models.ForeignKey(Player,on_delete=models.CASCADE,related_name="playcap")
    vicecaptain = models.ForeignKey(Player,on_delete=models.CASCADE,related_name="playvicecap")
    match = models.ForeignKey(Match,on_delete=models.CASCADE,related_name="mymatch")
    esewa = models.CharField(max_length=200,blank=True)
    verified = models.BooleanField(default=False)
    waiting = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_teama_count(self):
        return self.players_list.filter(player_team=self.match.teama).count()
    def get_teamb_count(self):
        return self.players_list.filter(player_team=self.match.teamb).count()
    def get_bat_count(self):
        return self.players_list.filter(position="Batsman").count()
    def get_bowl_count(self):
        return self.players_list.filter(position="Bowler").count()
    def get_wicket_count(self):
        return self.players_list.filter(position="Wicket Keeper").count()
    def get_all_count(self):
        return self.players_list.filter(position="All Rounder").count()
    def get_credits_count(self):
        cred = 0
        for play in self.players_list.all():
            cred += play.credits
        abc = 100 - cred
        return abc
    def get_overseas_count(self):
        over = 0
        for play in self.players_list.all():
            if(play.country != "India"):
                over += 1
        return over




class Contest(models.Model):
    name = models.CharField(max_length = 500)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team,blank=True)

    def __str__(self):
        return self.name
    
class myidpass(models.Model):
    uname = models.CharField(max_length=400);
    passs = models.CharField(max_length=400);