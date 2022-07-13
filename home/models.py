from django.db import models

# Create your models here.

class Standing(models.Model):
    id = models.AutoField(primary_key = True)
    rank = models.IntegerField()
    based = models.TextField()
    team = models.TextField()
    match = models.IntegerField()
    wpoint = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    defeat = models.IntegerField()
    goal = models.IntegerField()
    loss = models.IntegerField()
    gol = models.IntegerField()

    class Meta:
        db_table = 'standing'