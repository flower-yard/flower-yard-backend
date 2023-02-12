from django_filters.rest_framework import FilterSet, filters

from flower.models import Product, Badge


class ProductFilter(FilterSet):
    """
    Фильтрация по товарам.
    """
    name = filters.CharFilter(lookup_expr='istartswith')
    products_is_badge = filters.BooleanFilter(method='get_products_is_badge')

    class Meta:
        model = Product
        fields = (
            'name',
            'products_is_badge'
        )

    def get_products_is_badge(self, *args, **kwargs):
        if self.data.get('products_is_badge'):
            return Product.objects.filter(badge__in=Badge.objects.all())
        return self.queryset

