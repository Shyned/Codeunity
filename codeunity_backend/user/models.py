from django.db import models

# Create your models here.


class UserModel(models.Model):
    user_name = models.CharField(max_length = 20, unique = True )
    first_name = models.CharField(max_length = 20, unique = True )
    last_name = models.CharField(max_length = 20 )
    date_of_birth = models.DateField()
    