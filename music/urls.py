urlpatterns = [
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
    path('songs/', SongListView.as_view(), name='song-list'),
]