from rest_framework import serializers

from .models import Post, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.ReadOnlyField(source='following.username')
    class Meta:
        fields = ('following', 'user')
        model = Follow