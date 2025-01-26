from django.db import models
# Create your models here.
class Team(models.Model):
    team_name=models.CharField(max_length=30) 
    team_title=models.CharField(max_length=30) 
    team_salary=models.FloatField() 
    team_pic=models.ImageField(upload_to='images/')

