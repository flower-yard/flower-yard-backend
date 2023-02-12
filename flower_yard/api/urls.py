from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BadgeViewSet,
    CatalogViewSet,
    get_document,
    ProductViewSet,
)
from message.views import (
    SendEmailView
)

v1_router = DefaultRouter()

v1_router.register('catalogs', CatalogViewSet, basename='catalogs')
v1_router.register('badges', BadgeViewSet, basename='badge')
v1_router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('v1/send_mail/', SendEmailView.as_view(), name='send_mail'),
    path('v1/documents/', get_document),
    path('v1/', include(v1_router.urls)),
]