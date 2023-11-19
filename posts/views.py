from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import response, status

from .models import Post
from tags.models import Tag
from users.models import User
from polls.models import Poll

from polls.serializers import PollSerializer
from .serializers import CatalogPostSerializer, PostSerializer, CreatePostsSerializer

root_pass_header_name = 'X-Password'


@api_view(['POST'])
@permission_classes([AllowAny])
def add_posts(request):
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
            record = Post.objects.create(title=post['title'], body=post['body'], link=post['link'], timestamp=post['timestamp'])

            for tag in post['tags']:
                record.tags.add(Tag.objects.get(name=tag['name']))
                record.save()

        return response.Response(
            {'message': "Post successfully created!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([AllowAny])
def drop_posts(request):
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
    
    Post.objects.all().delete()

    return response.Response(
        {'message': "Posts dropped successfully!"},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_posts(requst):
    posts = Post.objects.all()
    serializer = CatalogPostSerializer(data=list(posts), many=True)

    return response.Response(
        {'posts': serializer.data},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_filtered_posts(request):
    user = User.objects.get(pk=request.user.id)
    all_posts = Post.objects.all()
    serializer = None

    if not user.subscriptions.exists():
        serializer = CatalogPostSerializer(all_posts, many=True)

        return response.Response(
            {'posts': serializer.data},
            status=status.HTTP_200_OK
        )
    
    posts_to_send = []
    
    for post in all_posts:
        found = False
        for tag in post.tags.all():
            if tag in user.subscriptions.all():
                found = True
                break

        if found:
            posts_to_send.append(post)

    serializer = CatalogPostSerializer(posts_to_send, many=True)

    return response.Response(
        {'posts': serializer.data},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, post_id):
    post = None
    try:
        post = Post.objects.get(pk=post_id)
    except:
        return response.Response(
            {'message': "Post not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = PostSerializer(post)

    return response.Response(
        {"post": serializer.data},
        status=status.HTTP_200_OK
    )
