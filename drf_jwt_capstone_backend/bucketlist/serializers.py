from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bucketlist
        fields=['id', 'adventure', 'user_id']
        