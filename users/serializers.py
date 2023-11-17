from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from categories.serializers import CategorySerializer


class UserSerializer(serializers.ModelSerializer):
    subscriptions = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'subscriptions',)


class UpdateSubscriptionsSerializer(serializers.Serializer):
    categories = serializers.ListField(child=serializers.CharField())

class UpdateEmail(serializers.Serializer):
    new_email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())],)
