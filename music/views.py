from rest_framework import generics
from .models import Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer


class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
