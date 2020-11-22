from django.shortcuts import render ,get_object_or_404
from .models import Music , Album
from django.core.paginator import Paginator
# Create your views here.

def home(request):
  musics = Music.objects.filter(show=True)
 
  context ={
    'musics':musics
  }
  return render(request,'music/home.html',context)


def detail(request ,pk,slug):
  musics =get_object_or_404(Music , pk=pk , show= True) 
 
  context ={
    'music':musics
  }
  return render(request,'music/detail.html',context)
