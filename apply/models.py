from django.db import models
# Create your models here.
class Apply(models.Model):
    apply_fname=models.CharField(max_length=30) 
    apply_lname=models.CharField(max_length=30) 
    apply_email=models.CharField(max_length=30) 
    apply_gender=models.CharField(max_length=30) 
    apply_pincode=models.CharField(max_length=30) 
    apply_phone=models.IntegerField() 
    apply_position=models.TextField() 
    apply_date=models.DateField() 
    apply_address=models.TextField()
    apply_coverletter=models.TextField()
    apply_resume= models.ImageField(upload_to='images/')