from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import response, status

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def initialize_categories(request):
    authorization_header = None

    if 'X-Init-Password' not in request.headers:
        return response.Response(
            {'message': "This request is not authorized!"},
            status=status.HTTP_403_FORBIDDEN
        )
    else:
        authorization_header = request.headers.get('X-Init-Password')

    if authorization_header != "Djibouti":
        return response.Response(
            {'message': "This request is not authorized!"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    Category.objects.all().delete()

    categories = ["Alegeri", "Demonstrații", "Incidente"]
    Category.objects.bulk_create([Category(name=category) for category in categories])

    return response.Response(
        {'message': "Categories initialized successfully"},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return response.Response(
        {'categories': serializer.data}, 
        status=status.HTTP_200_OK
    )
