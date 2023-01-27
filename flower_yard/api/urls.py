from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BadgeViewSet, CategoriesViewSet, FlowerViewSet

v1_router = DefaultRouter()

v1_router.register('category', CategoriesViewSet)
v1_router.register('badge', BadgeViewSet)
v1_router.register('flower', FlowerViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
