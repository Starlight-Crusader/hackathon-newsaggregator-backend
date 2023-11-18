from rest_framework import serializers

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'options', 'votes',)

class CreatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('title', 'options',)
