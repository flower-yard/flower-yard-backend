from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .filters import CategoriesFilter, FlowerFilter
from .serializers import (BadgeSerializer, CategorySerializer,
                          DocumentsSerializer, FlowerSerializer,
                          )
from django_filters.rest_framework import DjangoFilterBackend
from flower.models import (Badge, Category, Documents, Product)


class BadgeViewSet(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    pagination_class = None


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriesFilter
    pagination_class = None


class FlowerViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = FlowerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FlowerFilter
    search_fields = ('^name',)


@api_view(['GET', ])
def get_document(request):
    serializer = DocumentsSerializer(Documents.objects.latest(), context={"request": request})
    return Response(serializer.data)

