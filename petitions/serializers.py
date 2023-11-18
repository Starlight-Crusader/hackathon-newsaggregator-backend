from rest_framework import serializers

from .models import Petition
from users.serializers import UserPetitionSerializer


class PetitionSerializer(serializers.ModelSerializer):
    creator = UserPetitionSerializer()

    class Meta:
        model = Petition
        fields = ('title', 'body', 'creator',)
