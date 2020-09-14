# Generated by Django 3.1.1 on 2020-09-12 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('image', models.FileField(upload_to='')),
                ('credits', models.FloatField(default=0)),
                ('points', models.FloatField(default=0)),
                ('position', models.CharField(choices=[('India', 'India'), ('Australlia', 'Australlia'), ('England', 'England'), ('New Zealand', 'New Zealand'), ('West Indies', 'West Indies')], default='India', max_length=200)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.franchise')),
            ],
        ),
    ]