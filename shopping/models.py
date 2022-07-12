from django.db import models

# Create your models here.

class Shopping(models.Model):
    id = models.AutoField(primary_key=True)
    based = models.CharField(max_length=256)
    hteam = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

    class Meta:
        db_table = 'shopping'