from .models import Trainer
from django.shortcuts import redirect, render
from .forms import TrainerRegistrationForm
# Create your views here.


def register_trainers(request):
    form=TrainerRegistrationForm
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainers.html",{"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request, 'trainers_list.html',{"trainers":trainers})

def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm(instance=trainer)
        
    return render(request, "edit_trainer.html", {"form":form})

def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})


def delete_student(request,id):
    trianer=Trainer.objects.get(id=id)
    trianer.delete()
    return redirect("trainers_list")
