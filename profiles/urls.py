from django.urls import path
from profiles.views import ProfileList, ProfileDetail, UserProfileMusicView

urlpatterns = [
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),
    path('profile/<int:user_id>/music/', UserProfileMusicView.as_view(), name='user-music'),
]
