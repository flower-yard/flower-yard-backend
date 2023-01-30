from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BadgeViewSet, CategoriesViewSet, CharacteristicViewSet, FlowerViewSet,
                    FlowerCharacteristicViewSet)

v1_router = DefaultRouter()

v1_router.register('category', CategoriesViewSet)
v1_router.register('badge', BadgeViewSet)
v1_router.register('flower', FlowerViewSet)
v1_router.register('characteristic', CharacteristicViewSet)
v1_router.register("flower-characteristic", FlowerCharacteristicViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
