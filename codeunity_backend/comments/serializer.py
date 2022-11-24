from rest_framework import serializers
from .models import CommentModel


class CommentSerializer(serializers.ModelSerializers):
    class Meta:
        Model = Comment
        fields = ['user', 'room','comment', ]
        depth = 2