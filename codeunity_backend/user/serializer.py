from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = ['auth_user', 'first_name', 'last_name']
        depth = 1