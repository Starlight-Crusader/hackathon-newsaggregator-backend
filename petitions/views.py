from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import response, status

from users.models import User
from .models import Petition
from .serializers import serializers


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_petition(request):
    user = User.objects.get(pk=request.user.id)
    # serializer = 