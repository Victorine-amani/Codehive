from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
  
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), 
    url(r'^event_form/$', views.event, name='event_form'), 
]
