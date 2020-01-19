from django.db import models


# Model of National Olympic Committee.
class NOC(models.Model):
    noc = models.TextField(primary_key=True,
                           unique=True,
                           blank=False,
                           null=False,
                           verbose_name="National Olympic Committee")
    country_name = models.TextField(max_length=50, verbose_name="Country name of NOC")
    notes = models.TextField(max_length=80, verbose_name="Notes about NOC or Country.", null=True, blank=True)


# Model of Athlete information's in the Olympic Events.
class Athlete(models.Model):
    SEX_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F')
    )
    MEDAL_CHOICES = (
        ('NOT APPLICABLE', 'NA'),
        ('GOLD', 'Gold'),
        ('SILVER', 'Silver'),
        ('BRONZE', 'Bronze')
    )

    athleteid = models.IntegerField(verbose_name="Athlete ID",
                                     max_length=None,
                                     blank=False, null=False)

    name = models.TextField(verbose_name="Name of Athlete", max_length=80, blank=False, null=False)
    sex = models.TextField(verbose_name="Sex of Athlete", max_length=6, choices=SEX_CHOICES)
    age = models.TextField(verbose_name="Age of Athlete", blank=False, null=False)
    height = models.TextField(verbose_name="Height of Athlete", blank=False, null=False)
    weight = models.TextField(verbose_name="Weight of Athlete", blank=False, null=False)
    team = models.TextField(verbose_name="Team of Athlete", blank=False, null=False)
    noc = models.ForeignKey(NOC, on_delete=models.CASCADE, db_column="noc")
    games = models.TextField(verbose_name="Year and season of event", max_length=20, blank=False, null=False)
    year = models.TextField(verbose_name="Year of Event", max_length=4, blank=False, null=False)
    season = models.TextField(verbose_name="Season of Event", max_length=15, blank=False, null=False)
    city = models.TextField(verbose_name="Host City of Event", max_length=50, blank=False, null=False)
    sport = models.TextField(verbose_name="Sport of Athlete", max_length=90, blank=False, null=False)
    event = models.TextField(verbose_name="Name of Event Participate", max_length=60, blank=False, null=False)
    medal = models.TextField(verbose_name="Medal win", choices=MEDAL_CHOICES, blank=False, null=False)
