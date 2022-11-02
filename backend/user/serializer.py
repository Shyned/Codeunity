from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = ['id','user_firebase_id', 'user_name', 'first_name', 'last_name','date_of_birth']
        depth = 1