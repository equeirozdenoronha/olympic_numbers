# Generated by Django 3.0.2 on 2020-01-17 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NOC',
            fields=[
                ('noc', models.TextField(primary_key=True, serialize=False, unique=True, verbose_name='National Olympic Committee')),
                ('country_name', models.TextField(max_length=50, verbose_name='Country name of NOC')),
                ('notes', models.TextField(max_length=80, verbose_name='Notes about NOC or Country.')),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('athlete_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Athlete ID')),
                ('name', models.TextField(max_length=80, verbose_name='Name of Athlete')),
                ('sex', models.TextField(choices=[('Male', 'M'), ('Female', 'F')], max_length=6, verbose_name='Sex of Athlete')),
                ('age', models.IntegerField(verbose_name='Age of Athlete')),
                ('height', models.IntegerField(verbose_name='Height of Athlete')),
                ('weight', models.IntegerField(verbose_name='Weight of Athlete')),
                ('team', models.TextField(verbose_name='Team of Athlete')),
                ('games', models.TextField(max_length=20, verbose_name='Year and season of event')),
                ('year', models.TextField(max_length=4, verbose_name='Year of Event')),
                ('season', models.TextField(max_length=15, verbose_name='Season of Event')),
                ('city', models.TextField(max_length=50, verbose_name='Host City of Event')),
                ('sport', models.TextField(max_length=90, verbose_name='Sport of Athlete')),
                ('event', models.TextField(max_length=60, verbose_name='Name of Event Participate')),
                ('medal', models.TextField(choices=[('NOT APPLICABLE', 'NA'), ('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], verbose_name='Medal win')),
                ('noc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NOC', to='olympic.NOC')),
            ],
        ),
    ]