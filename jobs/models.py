from django.db import models
# Create your models here.
class Job(models.Model):
    job_title=models.CharField(max_length=30) 
    job_location=models.CharField(max_length=30) 
    job_salary=models.FloatField() 
    job_type=models.CharField(max_length=30) 
    job_desc=models.TextField() 
    job_pic = models.ImageField(upload_to='images/')


