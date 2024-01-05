from django.urls import path
from music.views import AlbumListView, ReviewList, ReviewDetail


urlpatterns = [
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
]