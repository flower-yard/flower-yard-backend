from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (BadgeSerializer, CategorySerializer,
                          CharacteristicSerializer,
                          FlowerSerializer, FlowerCharacteristicSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from flower.models import Badge, Category, Characteristic, Flower, FlowerCharacteristic


class BadgeViewSet(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    lookup_field = 'slug'


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class FlowerViewSet(ReadOnlyModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = (filters.SearchFilter, )
    search_name = ('name', )


class CharacteristicViewSet(ReadOnlyModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class FlowerCharacteristicViewSet(ReadOnlyModelViewSet):
    queryset = FlowerCharacteristic.objects.all()
    serializer_class = FlowerCharacteristicSerializer
    filter_backends = (DjangoFilterBackend, )



