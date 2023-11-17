from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import response, status

from .serializers import RegisterSerializer, LoginSerializer
from users.models import User

from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(requset):
    serializer = RegisterSerializer(data=requset.data)
    serializer.is_valid(raise_exeption=True)

    try:
        serializer.save()
        return response.Response(
            {'message': "User registered successfully!"},
            status=status.HTTP_201_CREATED
        )
    except:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = None

    try:
        user = User.objects.get(username=serializer.data['username'])
    except User.DoesNotExist:
        return response.Response(
            {'message': "User does not exist!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if user.check_password(serializer.data['password']) is False:
        return response.Response(
            {'message': "Password is incorrect!"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    refresh = RefreshToken.for_user(user=user)
    tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    return response.Response(
        {'tokens': tokens},
        status=status.HTTP_202_ACCEPTED
    )
