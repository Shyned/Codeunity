from django.shortcuts import render
from django.shortcuts import get_object_or_404
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#
from .models import ChatroomModel
from chatroom.serializer import ChatroomSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_chatrooms(request):
    all_chatrooms = ChatroomModel.objects
    serializer = ChatroomSerializer( all_chatrooms, many = True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chatroom(request,pk):
    selected_chatroom = ChatroomModel.objects.get(name = pk)
    serializer = ChatroomSerializer(selected_chatroom)
    return Response(serializer.data)