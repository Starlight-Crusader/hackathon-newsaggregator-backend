from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import response, status

from .models import Poll
from posts.models import Post
from users.models import User
from .serializers import CreatePollSerializer


root_pass_header_name = 'X-Password'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll(request, post_id):
    serializer = CreatePollSerializer(data=request.data)

    if serializer.is_valid():
        user = User.objects.get(id=request.user.id)
        title = serializer.validated_data.get('title', [])
        options = serializer.validated_data.get('options', [])
        to_post = Post.objects.get(pk=post_id)

        votes = []
        for option in options:
            votes.append(0)

        record = Poll.objects.create(title=title, creator=user, options=options, votes=votes, to_post=to_post)

        return response.Response(
            {'message': "Poll added successfully!"},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def approve_poll(request, poll_id):
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
    
    record = Poll.objects.get(pk=poll_id)
    record.approved = True
    record.save()

    return response.Response(
        {'message': "Poll successfully approved!"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def drop_polls(request):
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
    
    Poll.objects.delete().all()

    return response.Response(
        {'message': "Polls dropped successfully!"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def count_vote(request, poll_id, option):
    user = User.objects.get(pk=request.user.id)

    poll = None

    try:
        poll = Poll.objects.get(pk=poll_id)
    except:
        return response.Response(
            {'message': "Poll not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    poll.votes[option] += 1
    poll.save()

    return response.Response(
        {'message': "Vote counted!"},
        status=status.HTTP_200_OK
    )
