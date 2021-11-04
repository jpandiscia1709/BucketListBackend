from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.

class Bucketlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adventure = models.CharField(max_length=100)
