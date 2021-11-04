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



@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_bucketlists(request):
    bucketlist = Bucketlist.objects.all()
    serializer = BucketlistSerializer(bucketlist, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_bucketlist(request):
    if request.method == 'POST':
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        bucketlist = Bucketlist.objects.filter(user_id=request.user.id)
        serializer = BucketlistSerializer(bucketlist, many=True)
        return Response(serializer.data)




# class BucketList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         bucketlist = Bucketlist.objects.all()
#         serializer = BucketlistSerializer(bucketlist, many=True)
#         return Response(serializer.data)