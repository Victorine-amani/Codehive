from .models import Course
from django.shortcuts import render
from .forms import CoursesCreationForm
# Create your views here.

def courses(request):
    form=CoursesCreationForm
    if request.method=="POST":
        form=CoursesCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=CoursesCreationForm()
    return render(request,"courses.html",{"form":form}) 

def courses_list(request):
    courses=Course.objects.all()
    return render(request, 'courses_list.html',{"courses":courses}) 





