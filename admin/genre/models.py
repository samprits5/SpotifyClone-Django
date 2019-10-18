from django.db import models

# Create your models here.


class Genre(models.Model):

    genre_name = models.CharField(max_length=50)
    genre_des = models.CharField(max_length=150, default="This is a Popular Genre!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.genre_name
