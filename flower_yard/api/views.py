from rest_framework.viewsets import ReadOnlyModelViewSet
from .filters import CategoriesFilter, FlowerFilter
from .serializers import (BadgeSerializer, CategorySerializer,
                          CharacteristicSerializer,
                          FlowerSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from flower.models import (Badge, Category,
                           Characteristic, Product)


class BadgeViewSet(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriesFilter
    filterset_fields = ['slug']


class FlowerViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FlowerFilter
    search_fields = ('^name',)


class CharacteristicViewSet(ReadOnlyModelViewSet):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
