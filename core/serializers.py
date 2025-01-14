from rest_framework import serializers
from .models import ModelItem

class ModelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelItem
        fields = '__all__'
