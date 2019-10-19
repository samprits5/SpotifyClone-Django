from django.db import models
from admin.genre.models import Genre
from admin.mood.models import Mood
from admin.artist.models import Artist
# Create your models here.


class Song(models.Model):

    song_name = models.CharField(max_length=50)
    song_des = models.CharField(max_length=150, default="This is a Popular Song!")

    song_length = models.CharField(max_length=10)

    song_file = models.FileField(upload_to='songs/')

    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    mood_name = models.ForeignKey(Mood, on_delete=models.CASCADE)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.song_name





