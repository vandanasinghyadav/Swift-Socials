from django.db import models
# Create your models here.
class User(models.Model):
    user_email=models.CharField(max_length=30) 
    user_password=models.CharField(max_length=30) 