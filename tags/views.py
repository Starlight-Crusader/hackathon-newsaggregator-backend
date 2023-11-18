from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import response, status

from .models import Tag
from .serializers import TagSerializer


root_pass_header_name = 'X-Password'


@api_view(['POST'])
@permission_classes([AllowAny])
def initialize_tags(request):
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
    
    Tag.objects.all().delete()

    Tag.objects.create(name="Default", type=0)

    tags = ["Alegeri", "Economie", "Societate", "Demonstratii", "Politica"]
    Tag.objects.bulk_create([Tag(name=category, type=1) for category in tags])

    # tags = ["Chișinău", "Bălți"]
    # Tag.objects.bulk_create([Tag(name=category, type=2) for category in tags])

    return response.Response(
        {'message': "Tags initialized successfully"},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_tags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return response.Response(
        {'tags': serializer.data}, 
        status=status.HTTP_200_OK
    )
