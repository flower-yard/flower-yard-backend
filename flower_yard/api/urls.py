from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BadgeViewSet,
    CategoriesViewSet,
    FlowerViewSet,
)
from message.views import (
    SendEmailView
)

v1_router = DefaultRouter()

v1_router.register('categories', CategoriesViewSet)
v1_router.register('badges', BadgeViewSet)
v1_router.register('flowers', FlowerViewSet)

urlpatterns = [
    path('v1/send_mail/', SendEmailView.as_view(), name='send_mail'),
    path('v1/', include(v1_router.urls)),
]
