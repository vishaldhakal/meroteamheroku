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

class Team(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    players_list = models.ManyToManyField(Player,blank=True)
    
class Match(models.Model):
    match_no = models.IntegerField()
    teams = models.ManyToManyField(Team,blank=True)
    teama = models.ForeignKey(Franchise,on_delete=models.CASCADE,related_name="teama")
    teamb = models.ForeignKey(Franchise,on_delete=models.CASCADE,related_name="teamb")
    match_date = models.DateTimeField(auto_now_add=False,auto_now=False)


class Contest(models.Model):
    name = models.CharField(max_length = 500)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    
