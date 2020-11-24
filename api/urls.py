from django.urls import path 
from .views import BlogAPIView ,MusicAPIView ,AlbumAPIView

app_name ='api'

urlpatterns = [
path('',BlogAPIView.as_view(), name='blog_api' ),
path('music/',MusicAPIView.as_view(), name='music_api' ),
path('album/',AlbumAPIView.as_view(), name='album_api' ),
]
