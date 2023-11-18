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
        fields = ('title', 'body', 'link', 'timestamp', 'tags', 'polls_attached',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['polls_attached'] = instance.attached_polls.all().values()

        return data


class CreatePostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'link', 'timestamp', 'tags',)


class CreatePostsSerializer(serializers.Serializer):
    posts = CreatePostSerializer(many=True)


class CatalogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'timestamp',)
