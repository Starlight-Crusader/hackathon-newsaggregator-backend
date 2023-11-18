from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'options', 'votes', 'creator',)

class CreatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('title', 'options',)
