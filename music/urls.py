from django.urls import path
from music.views import ArtistListView, AlbumListView


urlpatterns = [
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
]