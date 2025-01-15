from rest_framework import serializers
from .models import ModelMajor, ModelUser

class ModelMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMajor
        fields = '__all__'

class ModelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = '__all__'
