from django.shortcuts import get_object_or_404
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#
from .models import CommentModel 
from comments.serializer import CommentSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chatroom_comments(request,pk):
    chatroom_comments = CommentModel.objects.get(name = pk)
    serializer = CommentSerializer(chatroom_comments)
    return Response(serializer.data)