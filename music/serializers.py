from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Album , Music

class MusicSerializer(ModelSerializer):
    class Meta:
        model = music
        fields= ["name","rapper","slug","cover",
        "publish_time","update","label",'des',
        ]



class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields= [
        "name","rapper","slug","cover",
        "publish_time","label",
        ]
