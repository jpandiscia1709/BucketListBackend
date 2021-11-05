from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from adventures.models import Adventure 
User = get_user_model()


# Create your models here.


class Bucketlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)


class Reviews(models.Model):
    adventure = models.ForeignKey(Bucketlist, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField
    comment = models.TextField

class Community(models.Model):
    adventure = models.ForeignKey(Bucketlist, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interested = models.BooleanField(default=False)

