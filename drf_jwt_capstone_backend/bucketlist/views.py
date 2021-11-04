from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bucketlist
from .serializers import BucketlistSerializer
from django.contrib.auth import get_user_model
User = get_user_model()




class BucketList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        bucketlist = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlist, many=True)
        return Response(serializer.data)