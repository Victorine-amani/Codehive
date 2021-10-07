from django.db import models


# Create your models here.



class Course(models.Model):

    name=models.CharField(max_length=30)
    code=models.CharField(max_length=10)
    description=models.TextField()
    trainer=models.CharField(max_length=25)
    
    
  


