from xml.etree.ElementTree import Comment
from django.forms import ModelChoiceField
from platformdirs import user_cache_dir
from rest_framework import serializers
from models import CommentsModel



class CommentSerializer(serializers.ModelSerializers):
    class Meta:
        Model = Comment
        fields = ['user', 'room','comment', ]
        depth = 2