from django.db import models

# Create your models here.

Gender=(
    ("Kenyan","Kenyan"),
    ("Ugandan","Ugandan"),
    ("Rwandese","Rwandese"),
    ("South Sudanese","South Sudanese"),
    ("Tanzanian","Tanzanian")
)
Nationality=(
    ("Female","Female"),
    ("Male","Male"),
    ("Binary","Binary"),
    ("Do not specify","Do not specify"),
    ("THey/Them","THey/Them")
)

class Trainer(models.Model):

    
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    course=models.CharField(max_length=35)
    identification=models.CharField(max_length=13)
    gender=models.CharField(max_length=20, choices=Nationality, default="Female")
    phone_number=models.CharField(max_length=15)
    nationality=models.CharField(max_length=20,  choices=Gender, default="Kenyan")
    email=models.EmailField()
    city=models.CharField(max_length=15)
    salary=models.PositiveBigIntegerField(null=True)
    resume=models.FileField(upload_to='document/%Y/%m/%d')
    profile_picture= models.ImageField(upload_to='images/%Y/%m/%d')
  