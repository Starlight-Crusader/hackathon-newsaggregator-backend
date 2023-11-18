from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import response, status

from .models import Post
from .serializers import CreatePostsSerializer

root_pass_header_name = 'X-Password'


@api_view(['POST'])
@permission_classes([AllowAny])
def add_posts(request):
    print(request.data)
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
    
    serializer = CreatePostsSerializer(data=request.data)
    if serializer.is_valid():
        for post in serializer.validated_data.get('posts', []):
            Post.objects.create(post)

        return response.Response(
            {'message': "Poll successfully approved!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

