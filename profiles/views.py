from django.db.models import Count
from rest_framework import generics, filters
from django.views import View
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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Explicitly set favourite_artist and favourite_album during the update
        serializer.save(favourite_artist=request.data.get('favourite_artist'),
                        favourite_album=request.data.get('favourite_album'))

        return Response(serializer.data)


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