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

@api_view(["GET", "DElETE"])
@permission_classes([IsAuthenticated])
def get_chatroom(request,pk):
    selected_chatroom = ChatroomModel.objects.get(name = pk)
    if request.method == "GET":
        serializer = ChatroomSerializer(selected_chatroom)
        return Response(serializer.data)
    elif request.method  == "DELETE":
        creator_room = selected_chatroom.objects.filter(room_creator=request.user)
        creator_room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_chat_room(request):
    serializer = ChatroomSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)