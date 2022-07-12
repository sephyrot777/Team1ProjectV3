from django.db import models

# Create your models here.

class Records(models.Model):
    id = models.AutoField(primary_key = True)
    rank = models.IntegerField()
    name = models.TextField()
    team = models.TextField()
    goal = models.IntegerField()
    assist = models.IntegerField()
    attackpoint = models.IntegerField()
    losspoint = models.IntegerField()
    cornerkick = models.IntegerField()
    foul = models.IntegerField()
    shoot = models.IntegerField()
    offside = models.IntegerField()
    warning = models.IntegerField()
    exit = models.IntegerField()
    norun = models.IntegerField()
    trip = models.IntegerField()
    replace = models.IntegerField()
    matchpoint = models.FloatField()

    class Meta:
        db_table = 'records'


class Soccers(models.Model):
    id = models.AutoField(primary_key = True)
    team = models.TextField()
    number = models.IntegerField()
    name = models.TextField()
    height = models.TextField()
    kg = models.TextField()
    birth = models.TextField()
    position = models.TextField()

    class Meta:
        db_table = 'soccers'


