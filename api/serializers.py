from rest_framework import serializers

from admin.song.models import Song

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'song_length')