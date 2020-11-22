from django.shortcuts import render
from .models import Blog


def home(request):
  return render(request,'blog/index.html',{})


