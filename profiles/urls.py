from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
     path('profile/<int:user_id>/music/', UserProfileMusicView.as_view(), name='user-music'),
]