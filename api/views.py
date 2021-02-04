from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .serializers import CommentSerializer, PostSerializer, FollowSerializer, GroupSerializer
from .models import Post, Comment, Follow, User, Group
from rest_framework.permissions import (IsAuthenticated)
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    http_method_names = ('get', 'post')
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', ]
    #queryset = Follow.getobject.all()

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)



class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ('get', 'post')