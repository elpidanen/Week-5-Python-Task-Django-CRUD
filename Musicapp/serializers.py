from rest_framework import serializers

from Musicapp.models import Artiste, Lyric, Song
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'date_releases', 'likes', 'artiste_id')

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('id', 'content', 'song_id')