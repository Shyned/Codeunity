from django.shortcuts import render
from chatroom.serializer import ChatroomSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ChatroomModel




