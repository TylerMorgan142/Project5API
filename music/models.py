# music/models.py

from django.db import models
from django.apps import apps

class Artist(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

