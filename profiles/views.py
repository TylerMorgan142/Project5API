from django.db.models import Count
from rest_framework import generics, filters
from django.views import View
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from Metalhub_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


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
            'favourite_artist': {
                'id': user_profile.favourite_artist.id,
                'name': user_profile.favourite_artist.name,
            } if user_profile.favourite_artist else None,
            'favourite_album': {
                'id': user_profile.favourite_album.id,
                'title': user_profile.favourite_album.title,
            } if user_profile.favourite_album else None,
        }
        return JsonResponse(data)

    def put(self, request, user_id):
        user_profile = get_object_or_404(Profile, owner__id=user_id)

        # Get the primary key values from the request data
        favourite_artist_pk = request.data.get('favourite_artist', None)
        favourite_album_pk = request.data.get('favourite_album', None)

        # Update the user profile with the provided favourite_artist and favourite_album
        user_profile.favourite_artist_id = favourite_artist_pk
        user_profile.favourite_album_id = favourite_album_pk
        user_profile.save()

        # Serialize and return the updated profile
        serializer = ProfileSerializer(user_profile)
        return JsonResponse(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_music_view(request, user_id):
    view = UserProfileMusicView.as_view()
    return view(request, user_id)