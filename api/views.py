from django.shortcuts import render

from blog.models import Blog ,Category 
from music.models import Music , Album
from rest_framework  import generics
from .serializers import BlogSerializer ,MusicSerializer ,AlbumSerializer

class BlogAPIView(generics.ListAPIView):
  queryset = Blog.objects.filter(status= 'p')
  serializer_class  = BlogSerializer


class MusicAPIView(generics.ListAPIView):
  queryset = Music.objects.filter(show= True)
  serializer_class  = MusicSerializer


class AlbumAPIView(generics.ListAPIView):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer