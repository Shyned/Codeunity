from unittest.util import _MAX_LENGTH
from django.db import models
from user.models import UserModel
# Create your models here.
class ChatroomModel(models.Model):
    room_id = models.CharField(max_length = 20 )
    room_creator = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name='creator')
    guest = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name='guest')
    youtube_video_id = models.CharField(max_length = 500)
    