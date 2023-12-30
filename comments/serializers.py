from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from music.models import Review
from posts.models import Post
from music.serializers import AlbumSerializer
from posts.serializers import PostSerializer
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_post(self, obj):
        if obj.post:
            post_data = {
                'id': obj.post.id,
                'title': obj.post.title,
                'content': obj.post.content,
            }
            return PostSerializer(post_data).data
        return None

    def get_review(self, obj):
        if obj.review:
            review_data = {
                'id': obj.review.id,
                'owner': obj.review.owner.username,
                'album': AlbumSerializer(obj.review.album).data,
                'rating': obj.review.rating,
                'title': obj.review.title,
                'content': obj.review.content,
            }
            return review_data
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'review', 'created_at', 'updated_at', 'content'
        ]



class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')