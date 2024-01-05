from django.contrib import admin
from .models import Album, Review

admin.site.register(Review)
admin.site.register(Album)