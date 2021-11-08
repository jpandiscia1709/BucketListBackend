from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Adventure
from .serializers import AdventureSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_adventures(request):
    adventure = Adventure.objects.all()
    serializer = AdventureSerializer(adventure, many=True)
    return Response(serializer.data)
