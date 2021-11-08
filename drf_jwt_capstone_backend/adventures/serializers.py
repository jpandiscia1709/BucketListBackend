from rest_framework import serializers
from .models import Adventure, Company

class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model= Adventure
        fields=['id', 'location', 'duration', 'price', 'company_id']
        # model = Company
        # fields=['name', 'company_url']
        
