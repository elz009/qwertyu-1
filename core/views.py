from rest_framework import viewsets
from .models import ModelItem
from .serializers import ModelItemSerializer

class ModelItemViewSet(viewsets.ModelViewSet):
    queryset = ModelItem.objects.all()
    serializer_class = ModelItemSerializer
