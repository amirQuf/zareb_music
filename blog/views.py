from django.shortcuts import render
from .models import Blog


def home(request):
  blogs = Blog.objects.filter(status='p')
  return render(request,'blog/index.html',{
    'blogs':blogs
  })


def detail(request ,pk , slug):
  blogs = Blog.objects.filter(status='p' ,pk= pk )
  return render(request,'blog/detail.html',{
    'blogs':blogs
  })

