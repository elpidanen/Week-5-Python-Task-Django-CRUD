from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    
class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length=1000)
    date_released = models.DateField()
    likes = models.IntegerField()
    

class Lyric(models.Model):
    content = models.CharField(max_length=4000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)