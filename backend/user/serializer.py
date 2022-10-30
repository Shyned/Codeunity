from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.Modelserializer):
    class Meta:
        model = UserModel,
        fields = ['user_firebase_id', 'username', 'first_name', 'last_name','date_of_birth']
        depth = 1