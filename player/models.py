from django.db import models
from team.models import Team
from datetime import date, timedelta


# Create your models here.

class Player(models.Model):
    
    name=models.TextField()
    team = models.ForeignKey(Team, related_name="team", on_delete=models.CASCADE)
    birth_date=models.DateField()
    value = models.FloatField()
    position=models.TextField()
    
    appearances = models.IntegerField()
    goals=models.IntegerField()
    assists=models.IntegerField()

    pace=models.IntegerField()
    shooting=models.IntegerField()
    passing=models.IntegerField()
    dribbling=models.IntegerField()
    defence=models.IntegerField()
    physical=models.IntegerField()
    


    def __str__(self):
       return "{}".format(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def getAge(self): 
        return (date.today() - self.birth_date)//timedelta(days=365.2425)
    
    class Meta:
        ordering = ['position']