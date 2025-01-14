from django.contrib import admin
from .models import (
    ModelUser,
    ModelStore,
    ModelItem,
    ModelOrder,
    ModelCartItem,
    ModelMajor,
    ModelCategory,
    ModelCity,
    ModelAddress,
    ModelAdditional,
    ModelWorkingHours,
    ModelStory,
    ModelNews
)


admin.site.register(ModelUser)
admin.site.register(ModelStore)
admin.site.register(ModelItem)
admin.site.register(ModelOrder)
admin.site.register(ModelCartItem)
admin.site.register(ModelMajor)
admin.site.register(ModelCategory)
admin.site.register(ModelCity)
admin.site.register(ModelAddress)
admin.site.register(ModelAdditional)
admin.site.register(ModelWorkingHours)
admin.site.register(ModelStory)
admin.site.register(ModelNews)
