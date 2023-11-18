from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import response, status

from .models import Post

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
    
    

    return response.Response(
        {'message': "Poll successfully approved!"},
        status=status.HTTP_200_OK
    )

