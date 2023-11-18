from rest_framework import serializers
from .models import Post

from polls.serializers import PollSerializer
from polls.models import Poll


class PostSerializer(serializers.ModelSerializer):
    polls_attached = PollSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'timestamp', 'polls_attached']
