from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from trainers.models import Trainer
from student.models import Student
from courses.models import Course
from events.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name', 'last_name','age')

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=('first_name', 'last_name','email')
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('name', 'code','trainer')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"