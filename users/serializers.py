from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from tags.serializers import TagSerializer


class UserSerializer(serializers.ModelSerializer):
    subscriptions = TagSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'subscriptions', 'email', )

class UserPetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_verified')

class UpdateSubscriptionsSerializer(serializers.Serializer):
    tags = serializers.ListField(child=serializers.CharField(),)

class UpdateEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())],)
