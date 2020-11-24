from rest_framework import serializers


from blog.models import Blog ,Category 

from music.models import Music , Album

class  BlogSerializer (serializers.ModelSerializer):
  class Meta:
    model = Blog 
    fields =('title','cover','desc','slug','publish_time','category',"status")

class MusicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Music 
    fields=('name','rapper','album','label','mix_mastering','cover','cover_art','file','slug','publish_time','des',)

class AlbumSerializer(serializers.ModelSerializer):
  class Meta :
    model = Album
    fields=('name','rapper','label','cover','slug','publish_time')


