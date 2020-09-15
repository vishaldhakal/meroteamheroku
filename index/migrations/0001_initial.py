# Generated by Django 3.1.1 on 2020-09-14 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('net_run_rate', models.FloatField(default=0.0)),
                ('match_played', models.IntegerField(default=0)),
                ('match_won', models.IntegerField(default=0)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_no', models.IntegerField()),
                ('match_date', models.DateTimeField()),
                ('teama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teama', to='index.franchise')),
                ('teamb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamb', to='index.franchise')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('image', models.FileField(default='virat.png', upload_to='')),
                ('credits', models.FloatField(default=0)),
                ('points', models.FloatField(default=0)),
                ('position', models.CharField(choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('Wicket Keeper', 'Wicket Keeper'), ('All Rounder', 'All Rounder')], default='Batsman', max_length=200)),
                ('country', models.CharField(choices=[('India', 'India'), ('Australlia', 'Australlia'), ('England', 'England'), ('New Zealand', 'New Zealand'), ('West Indies', 'West Indies')], default='India', max_length=200)),
                ('player_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.franchise')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playcap', to='index.player')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mymatch', to='index.match')),
                ('players_list', models.ManyToManyField(blank=True, to='index.Player')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vicecaptain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playvicecap', to='index.player')),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.match')),
            ],
        ),
    ]
