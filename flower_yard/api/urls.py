from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BadgeViewSet,
    CategoriesViewSet,
    CharacteristicViewSet,
    FlowerViewSet
)

v1_router = DefaultRouter()

v1_router.register('categories', CategoriesViewSet)
v1_router.register('badges', BadgeViewSet)
v1_router.register('flowers', FlowerViewSet)
v1_router.register('characteristics', CharacteristicViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
