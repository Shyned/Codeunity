from django.db import models
from user.models import UserModel
from chatroom.models import ChatroomModel
# Create your models here.
class CommentModel (models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatroomModel,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 500)