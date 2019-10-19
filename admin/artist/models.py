from django.db import models

# Create your models here.


class Artist(models.Model):

    artist_name = models.CharField(max_length=50)
    artist_des = models.CharField(max_length=150, default="A Popular Artist!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.artist_name