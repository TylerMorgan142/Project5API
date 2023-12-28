from django.urls import path
from music.views import  ArtistListView, AlbumListView, ArtistCreateView, AlbumCreateView


urlpatterns = [
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
    path('artists/create/', ArtistCreateView.as_view(), name='create_artist'),
    path('albums/create/', AlbumCreateView.as_view(), name='create_album'),
]