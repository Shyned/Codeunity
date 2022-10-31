from django.shortcuts import render
# 
from user.serializer import UserSerializer
# 
from .models import UserModel
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = UserModel.objects.filter(user_firebase_id = request.fire_base_id)
    serializer = UserSerializer(user,many= False)
    return Response(serializer.data)