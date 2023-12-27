
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.apps import apps

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    favourite_artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE, null=True, blank=True)
    favourite_album = models.ForeignKey('music.Album', on_delete=models.CASCADE, null=True, blank=True)
    favourite_song = models.ForeignKey('music.Song', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_bbjdnr'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
