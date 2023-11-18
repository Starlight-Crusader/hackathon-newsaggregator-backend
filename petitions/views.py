from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import response, status

from users.models import User
from .models import Petition
from .serializers import CreatePetitionSerializer


root_pass_header_name = 'X-Password'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_petition(request):
    user = User.objects.get(pk=request.user.id)
    serializer = CreatePetitionSerializer(data=request.data)

    if serializer.is_valid():
        Petition.objects.create(
            title=serializer.validated_data['title'], 
            body=serializer.validated_data['body'],
            creator=user,
            voted=[user]
        )

        return response.Response(
            {'message': "Petition created successfully!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def approve_petition(request, petition_id):
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
    
    try:
        record = Petition.objects.get(pk=petition_id)
    except Petition.DoesNotExist:
        return response.Response(
            {'message': "Petition not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    record.is_approved = True
    record.save()

    return response.Response(
        {'message': "Petition approved succsessfully!"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def count_sub(request, petition_id):
    user = User.objects.get(pk=request.user.id)

    record = None

    try:
        record = Petition.objects.get(pk=petition_id)
    except:
        return response.Response(
            {'message': "Petition not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if user not in record.voted:
        record.voted.add(user)

        return response.Response(
            {'message': "Sub. counted!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': "You've already sub-ed under this petition!"},
            status=status.HTTP_403_FORBIDDEN
        )


@api_view(['DELETE'])
@permission_classes([AllowAny])
def drop_petitions(request):
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
    
    Petition.objects.all().delete()
    
    return response.Response(
        {'message': "Petitions dropped successfully!"},
        status=status.HTTP_200_OK
    )
