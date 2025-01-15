from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ModelMajorViewSet, ModelUserViewSet, ModelItemViewSet, ModelCityViewSet,
    ModelAddressViewSet, ModelStoreViewSet, ModelCategoryViewSet,
    ModelAdditionalViewSet, ModelWorkingHoursViewSet, ModelStoryViewSet,
    ModelNewsViewSet, ModelOrderViewSet, ModelCartItemViewSet
)

router = DefaultRouter()
router.register(r'majors', ModelMajorViewSet)
router.register(r'users', ModelUserViewSet)
router.register(r'items', ModelItemViewSet)
router.register(r'cities', ModelCityViewSet)
router.register(r'addresses', ModelAddressViewSet)
router.register(r'stores', ModelStoreViewSet)
router.register(r'categories', ModelCategoryViewSet)
router.register(r'additionals', ModelAdditionalViewSet)
router.register(r'working-hours', ModelWorkingHoursViewSet)
router.register(r'stories', ModelStoryViewSet)
router.register(r'news', ModelNewsViewSet)
router.register(r'orders', ModelOrderViewSet)
router.register(r'cart-items', ModelCartItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
