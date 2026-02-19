from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    # ... previous urls
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]