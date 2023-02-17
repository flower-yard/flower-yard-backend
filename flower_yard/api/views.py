from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from flower.models import (Badge, Category, Documents, Product)
from .filters import ProductFilter
from .serializers import (BadgeSerializer, CatalogDetailSerializer, CatalogListSerializer, DocumentsSerializer,
                          ProductDetailSerializer, ProductViewSerializer)


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
    serializer_class = ProductViewSerializer
    filterset_class = ProductFilter
    search_fields = ('^name',)
    lookup_field = 'category__slug'

    def retrieve(self, request, *args, **kwargs):
        serializer = (ProductDetailSerializer(
            Product.objects.filter(
                category__slug=self.kwargs.get('category__slug')),
            many=True))
        return Response(serializer.data)

    @action(methods=['get', ], detail=True,
            url_path='(?P<product__slug>[^/.]+)', url_name='products_slug')
    def get_product_by_slug(self, request, *args, **kwargs):
        serializer = (ProductDetailSerializer(
            get_object_or_404(Product, slug=self.kwargs.get('product__slug'))))
        return Response(serializer.data)


@api_view(['GET', ])
def get_document(request):
    serializer = DocumentsSerializer(Documents.objects.latest(), context={"request": request})
    return Response(serializer.data)
