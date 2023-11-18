from rest_framework import serializers
from .models import Post

from polls.serializers import PollSerializer
from polls.models import Poll
from tags.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    polls_attached = PollSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'timestamp', 'tags', 'polls_attached']


class CreatePostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'timestamp', 'tags']


class CreatePostsSerializer(serializers.Serializer):
    posts = CreatePostSerializer(many=True)
