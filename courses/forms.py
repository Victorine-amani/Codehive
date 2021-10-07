from django import forms
from django.db.models import fields
from .models import Course

class CoursesCreationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"

        widgets={
        'description':forms.Textarea(attrs={'class':'form_control','id':'des2'}),
        }
