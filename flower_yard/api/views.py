from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from .filters import ProductFilter
from .serializers import (
    BadgeSerializer, CatalogListSerializer,
    DocumentsSerializer,
    ProductViewSerializer, ProductDetailSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from flower.models import (Badge, Category, Documents, Product)


class BadgeViewSet(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    pagination_class = None


class CatalogViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatalogListSerializer
    pagination_class = None
    lookup_field = 'slug'


class ProductViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ('^name',)
    lookup_field = 'slug'


class ProductCategoryViewSet(ProductViewSet,
                             mixins.RetrieveModelMixin):
    """Выдает товары по категории, так же выдает отдельный товар
    по слагу.
    """
    lookup_field = 'slug'
    serializer_class = ProductDetailSerializer

    def get_category(self):
        return get_object_or_404(
            Category, slug=self.kwargs.get('category_slug')
        )

    def get_queryset(self):
        return self.get_category().category


@api_view(['GET', ])
def get_document(request):
    serializer = DocumentsSerializer(Documents.objects.latest(),
                                     context={"request": request})
    return Response(serializer.data)


