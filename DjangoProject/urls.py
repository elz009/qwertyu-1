from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ModelItemViewSet


router = DefaultRouter()
router.register(r'modelitems', ModelItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
