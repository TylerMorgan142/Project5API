# music/models.py

from django.db import models
from django.apps import apps

class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

