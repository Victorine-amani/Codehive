from django.urls import path
from .views import edit_trainer, register_trainers, trainer_list


urlpatterns=[
   path("register/", register_trainers, name="register_trainers"),
   path("list/", trainer_list, name="trainers_list"),
   path("edit/<int:id>/", edit_trainer,name="edit_trainer"),
   path("profile/<int:id>/",edit_trainer,name="trainer_profile"),
   path("delete/<int:id>/", edit_trainer, name="delete_trainer")
       
]
