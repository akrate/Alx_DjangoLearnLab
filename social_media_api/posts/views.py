from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 1. Kan-jibo l-users li mtaba3hom l-user l-current
        following_users = self.request.user.following.all()
        # 2. Kan-filteriw l-posts li l-author dialhom f dak l-list
        return Post.objects.filter(author__in=following_users).order_by('-created_at')