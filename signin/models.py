from django.db import models
# Create your models here.
class Signin(models.Model):
    signin_name=models.CharField(max_length=30) 
    signin_email=models.CharField(max_length=30) 
    signin_password=models.CharField(max_length=30) 