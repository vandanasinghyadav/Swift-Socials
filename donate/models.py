from django.db import models
# Create your models here.
class Donate(models.Model):
    donate_number=models.IntegerField() 
    donate_holder=models.CharField(max_length=30) 
    donate_expiry=models.DateField() 
    donate_cvc=models.CharField(max_length=30)