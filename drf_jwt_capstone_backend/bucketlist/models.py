from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.

class Bucketlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adventure = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField
    phone = models.IntegerField
    zip = models.IntegerField
