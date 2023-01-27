from rest_framework import viewsets
from .serializers import (BadgeSerializer, CategorySerializer,
                          FlowerSerializer, ReadFlowerSerializer)
from flower.models import Badge, Category, Flower


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FlowerViewSet(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = ReadFlowerSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadFlowerSerializer
        return FlowerSerializer

