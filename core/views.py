from rest_framework import serializers, viewsets
from .models import (ModelMajor, ModelUser, ModelItem, ModelCity, ModelAddress, ModelStore, ModelCategory,
                      ModelAdditional, ModelWorkingHours, ModelStory, ModelNews, ModelOrder, ModelCartItem)

class ModelMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMajor
        fields = '__all__'

class ModelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = '__all__'

class ModelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelItem
        fields = '__all__'

class ModelCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCity
        fields = '__all__'

class ModelAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAddress
        fields = '__all__'

class ModelStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStore
        fields = '__all__'

class ModelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCategory
        fields = '__all__'

class ModelAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelAdditional
        fields = '__all__'

class ModelWorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelWorkingHours
        fields = '__all__'

class ModelStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStory
        fields = '__all__'

class ModelNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelNews
        fields = '__all__'

class ModelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelOrder
        fields = '__all__'

class ModelCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCartItem
        fields = '__all__'

class ModelMajorViewSet(viewsets.ModelViewSet):
    queryset = ModelMajor.objects.all()
    serializer_class = ModelMajorSerializer

class ModelUserViewSet(viewsets.ModelViewSet):
    queryset = ModelUser.objects.all()
    serializer_class = ModelUserSerializer

class ModelItemViewSet(viewsets.ModelViewSet):
    queryset = ModelItem.objects.all()
    serializer_class = ModelItemSerializer

class ModelCityViewSet(viewsets.ModelViewSet):
    queryset = ModelCity.objects.all()
    serializer_class = ModelCitySerializer

class ModelAddressViewSet(viewsets.ModelViewSet):
    queryset = ModelAddress.objects.all()
    serializer_class = ModelAddressSerializer

class ModelStoreViewSet(viewsets.ModelViewSet):
    queryset = ModelStore.objects.all()
    serializer_class = ModelStoreSerializer

class ModelCategoryViewSet(viewsets.ModelViewSet):
    queryset = ModelCategory.objects.all()
    serializer_class = ModelCategorySerializer

class ModelAdditionalViewSet(viewsets.ModelViewSet):
    queryset = ModelAdditional.objects.all()
    serializer_class = ModelAdditionalSerializer

class ModelWorkingHoursViewSet(viewsets.ModelViewSet):
    queryset = ModelWorkingHours.objects.all()
    serializer_class = ModelWorkingHoursSerializer

class ModelStoryViewSet(viewsets.ModelViewSet):
    queryset = ModelStory.objects.all()
    serializer_class = ModelStorySerializer

class ModelNewsViewSet(viewsets.ModelViewSet):
    queryset = ModelNews.objects.all()
    serializer_class = ModelNewsSerializer

class ModelOrderViewSet(viewsets.ModelViewSet):
    queryset = ModelOrder.objects.all()
    serializer_class = ModelOrderSerializer

class ModelCartItemViewSet(viewsets.ModelViewSet):
    queryset = ModelCartItem.objects.all()
    serializer_class = ModelCartItemSerializer
