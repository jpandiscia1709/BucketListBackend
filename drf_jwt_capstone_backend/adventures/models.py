from django.db import models
# from bucketlist.models import Bucketlist
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company_url = models.CharField(max_length=100)



class Adventure(models.Model):
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.CharField(max_length=25)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

