from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status

from .models import User
from posts.models import Category
from .serializers import UpdateSubscriptionsSerializer,  UpdateEmail


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_subscriptions(request):
    user = User.objects.get(id=request.user.id)
    serializer = UpdateSubscriptionsSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        user.subscriptions.clear()
        categories_names = serializer.validated_data.get('categories', [])
        
        for category_name in categories_names:
            category = Category.objects.get(name=category_name)
            user.subscriptions.add(category)

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
    serializer = UpdateEmail(instance=user, data=requset.data)

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
