from django.contrib import admin
from .models import Album , Music


class MusicAdmin(admin.ModelAdmin):
    list_display=('name','rapper','slug','publish_time','show',"mix_mastering","label")
    list_filter = ('show' , 'publish_time')
    search_fields =('slug','name', 'desc')
    ordering =['-publish_time', 'show']   

admin.site.register(Music,MusicAdmin)
class AlbumAdmin(admin.ModelAdmin):
    list_display=('name','slug','created','publish_time')
    list_filter = ('publish_time',)
    search_fields =('slug','name', 'desc')
    ordering =['-publish_time',] 
    

admin.site.register(Album,AlbumAdmin)