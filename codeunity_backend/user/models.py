from django.db import models
from authentication.models import User

class UserModel(models.Model):
    auth_user = models.ForeignKey(User, on_delete= models.CASCADE)
    first_name = models.CharField(max_length = 20, unique = True )
    last_name = models.CharField(max_length = 20 )

    