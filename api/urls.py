from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet
from .views import EventViewSet

router=routers.DefaultRouter()
router.register('students/', StudentViewSet)
router.register('trainers/', TrainerViewSet)
router.register('courses/', CourseViewSet)
router.register('events/', EventViewSet)

urlpatterns=[
    path('', include(router.urls)),
]