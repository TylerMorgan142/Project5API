# music/models.py

from django.db import models
from django.apps import apps

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey('music.Genre', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey('music.Album', on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return f"{self.album.artist.name} - {self.album.title} - {self.title}"
