from rest_framework import generics
from .models import Album, Review
from .serializers import AlbumSerializer, ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumCreateView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer