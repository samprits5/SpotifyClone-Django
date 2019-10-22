from django.db import models
from admin.user.models import CustomUser
from admin.song.models import Song

# Create your models here.

class Favorite(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
    	return "User ID : " + self.user_id + "Song ID : " + self.song_id