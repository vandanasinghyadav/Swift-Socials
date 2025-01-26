from django.db import models
# Create your models here.
class Contact(models.Model):
    contact_name=models.CharField(max_length=30) 
    contact_email=models.CharField(max_length=30) 
    contact_phone=models.IntegerField() 
    contact_messege=models.TextField()