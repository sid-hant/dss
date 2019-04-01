from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.TextField()
    team_logo = models.FileField(upload_to="media/team-pics",blank=True)

    def __str__(self):
       return "{}".format(self.team_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['team_name']