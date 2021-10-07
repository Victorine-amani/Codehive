from django.urls import path
from .views import courses, courses_list


urlpatterns=[
     path("register/", courses, name="courses"),
    path("list/", courses_list, name="course_list"),
    
 ]