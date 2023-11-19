from rest_framework import serializers

from .models import Petition
from users.serializers import UserPetitionSerializer


class PetitionSerializer(serializers.ModelSerializer):
    creator = UserPetitionSerializer()

    class Meta:
        model = Petition
        fields = ('title', 'body', 'creator',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['subs_num'] = instance.voted.values().count()
    
        return data


class CreatePetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petition
        fields = ('title', 'body',)