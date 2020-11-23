from django.urls import path 
from .views import home ,detail
app_name= 'blog'
urlpatterns = [
  path('',home, name= 'home'),
  path('<slug:slug>/<int:pk>/',detail, name= 'detail'),
]