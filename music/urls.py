from django.urls import path
from music.views import AlbumListView, AlbumCreateView, ReviewList, ReviewDetail


urlpatterns = [
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('reviews/create/', ReviewList.as_view(), name='review-create'),
    path('albums/', AlbumListView.as_view(), name='album-list'),
    path('albums/create/', AlbumCreateView.as_view(), name='create_album'),
]