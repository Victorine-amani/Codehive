from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
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
    ("They/Them","They/Them")
)
def current_year():
    return datetime.date.today().year


def max_value(value):
    return MaxValueValidator(current_year())(value)

    
class Student(models.Model):
   
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(null=True)
    class_name=models.CharField(max_length=9,null=True,blank=True)
    identification=models.CharField(max_length=13)
    gender=models.CharField(max_length=20, choices=Nationality, default="Female")
    nationality=models.CharField(max_length=20,  choices=Gender, default="Kenyan")
    room_number=models.PositiveSmallIntegerField(null=True,blank=True)
    guardian_phoneNumber=models.CharField(max_length=15)
    academic_year=models.PositiveSmallIntegerField(default=current_year())
    city=models.CharField(max_length=15)
    guardian_name=models.CharField(max_length=25)
    profile_picture= models.ImageField(upload_to='media/')
    medical_report=models.FileField(upload_to='media/')
    


def __str__(self):
    return self.first_name
   

   


    

    
    
