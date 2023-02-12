from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .filters import ProductFilter
from .serializers import (
    BadgeSerializer, CatalogListSerializer,
    DocumentsSerializer,
    CatalogDetailSerializer, ProductViewSerializer, ProductDetailSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from flower.models import (Badge, Category, Documents, Product)


class BadgeViewSet(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    pagination_class = None


class CatalogViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CatalogDetailSerializer
        return CatalogListSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ('^name',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductViewSerializer


@api_view(['GET', ])
def get_document(request):
    serializer = DocumentsSerializer(Documents.objects.latest(), context={"request": request})
    return Response(serializer.data)
