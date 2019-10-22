from django.db import models
from admin.song.models import Song
# Create your models here.


class Homepage(models.Model):

    name = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
    	return self.name
