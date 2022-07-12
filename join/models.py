from datetime import datetime

from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    userid=models.CharField(max_length=18, unique=True)
    passwd=models.CharField(max_length=18)
    nickname=models.CharField(max_length=18)
    team = models.CharField(max_length=50)
    name = models.CharField(max_length=18)
    birth = models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    email=models.TextField()
    zipcode=models.CharField(max_length=5)
    addr = models.TextField()
    mailing = models.BooleanField(default=False)
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='member'