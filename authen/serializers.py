from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.hashers import make_password

from users.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=False,
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )

    password = serializers.CharField(
        write_only=True,
        validators=[],
        required=True,
    )

    email = serializers.CharField(
        write_only=False,
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        user = User(**validated_data)
        user.save()

        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
