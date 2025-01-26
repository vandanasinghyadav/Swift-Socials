from django.db import models
# Create your models here.
class Login(models.Model):
    login_email=models.CharField(max_length=30) 
    login_password=models.CharField(max_length=30) 