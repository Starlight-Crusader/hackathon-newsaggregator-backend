from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import response, status

from .models import User
from tags.models import Tag
from .serializers import UpdateSubscriptionsSerializer, UpdateEmailSerializer, UpdateVerificationStatusSerializer


root_pass_header_name = 'X-Root-Password'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_subscriptions(request):
    user = User.objects.get(id=request.user.id)
    serializer = UpdateSubscriptionsSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        user.subscriptions.clear()
        tags_names = serializer.validated_data.get('tags', [])
        
        for tag_name in tags_names:
            tag = Tag.objects.get(name=tag_name)
            user.subscriptions.add(tag)

        return response.Response(
            {'message': "Subscriptions updated successfully!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_email(requset):
    user = User.objects.get(id=requset.id)
    serializer = UpdateEmailSerializer(instance=user, data=requset.data)

    if serializer.is_valid():
        user.email = serializer.validated_data['new_email']
        user.save()

        return response.Response(
            {'message': "Email updated successfully!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def update_verification_status(request, user_id):
    authorization_header = None

    if root_pass_header_name not in request.headers:
        return response.Response(
            {'message': "This request is not authorized!"},
            status=status.HTTP_403_FORBIDDEN
        )
    else:
        authorization_header = request.headers.get(root_pass_header_name)

    if authorization_header != "Djibouti":
        return response.Response(
            {'message': "This request is not authorized!"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    user = None

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return response.Response(
            {'error': "User not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = UpdateVerificationStatusSerializer(instance=user, data=request.data, partial=True)

    if serializer.is_valid():
        user.is_verified = serializer.validated_data['is_verified']
        user.save()
        return response.Response(
            {'message': "Verification status changed successfully!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
