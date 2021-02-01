from rest_framework import viewsets
from .serializers import CommentSerializer, PostSerializer
from .models import Post, Comment
from rest_framework.permissions import (IsAuthenticated)
from .permissions import IsOwnerOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
