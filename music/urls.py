from django.urls import path 
from .views import home

app_name ='music'

urlpatterns = [
  path('',home ,name ='home'),
]
