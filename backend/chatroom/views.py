from django.shortcuts import render
from chatroom.serializer import ChatroomSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ChatroomModel
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_chatrooms(request):
    chatrooms = ChatroomModel
    serializer = ChatroomSerializer(chatrooms)
    return Response(serializer.data)