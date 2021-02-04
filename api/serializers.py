from rest_framework import serializers

from .models import Post, Comment, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=False,
        queryset=User.objects.all()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        #queryset=User.objects.all()
    )
    class Meta:
        fields = '__all__'
        model = Follow

class GroupSerializer(serializers.ModelSerializer):
    #title = serializers.ReadOnlyField(source='title')

    class Meta:
        fields = '__all__'
        model = Group