from django.db.models import Count
from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from Metalhub_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

class UserProfileMusicView(View):
    def get(self, request, user_id):
        user_profile = get_object_or_404(Profile, owner__id=user_id)
        data = {
            'user_id': user_id,
            'favorite_band': {
                'id': user_profile.favorite_band.id,
                'name': user_profile.favorite_band.name,
            } if user_profile.favorite_band else None,
            'favorite_album': {
                'id': user_profile.favorite_album.id,
                'title': user_profile.favorite_album.title,
            } if user_profile.favorite_album else None,
            'favorite_song': {
                'id': user_profile.favorite_song.id,
                'title': user_profile.favorite_song.title,
            } if user_profile.favorite_song else None,
        }
        return JsonResponse(data)